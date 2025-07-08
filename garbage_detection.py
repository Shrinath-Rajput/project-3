import cv2
import numpy as np
import mysql.connector
import os
import datetime

# --- MySQL Connection ---
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="shrinath1818",
    database="student"
)
cursor = conn.cursor()

# --- Image Folder Setup ---
save_dir = "captured"
os.makedirs(save_dir, exist_ok=True)

# --- HSV Color Ranges ---
color_ranges = {
    "plastic": ((100, 150, 0), (140, 255, 255)),  # Blue
    "rubber": [((0, 100, 100), (10, 255, 255)), ((160, 100, 100), (179, 255, 255))],  # Red
    "weight": ((25, 50, 70), (35, 255, 255)),  # Yellow
    "dry": ((40, 40, 40), (80, 255, 255))  # Green
}

# --- Sample image map for each type ---
sample_image_map = {
    "plastic": r"C:\Users\DELL\Downloads\archive (1)\garbage-dataset\plastic\plastic_8.jpg",
    "rubber": r"C:\Users\DELL\Downloads\archive (1)\garbage-dataset\glass\glass_144.jpg",
    "weight": r"C:\Users\DELL\Downloads\archive (1)\garbage-dataset\biological\biological_5.jpg",
    "dry": r"C:\Users\DELL\Downloads\archive (1)\garbage-dataset\paper\paper_468.jpg"
}

# --- Start Camera ---
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("❌ Error: Cannot open camera.")
    exit()
print("🎥 Camera opened. Detecting garbage...")

detected_type = None
captured_frame = None

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to read frame.")
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    for garbage_type, bounds in color_ranges.items():
        if garbage_type == "rubber":
            mask = np.zeros(hsv.shape[:2], dtype=np.uint8)
            for lower, upper in bounds:
                mask += cv2.inRange(hsv, np.array(lower), np.array(upper))
        else:
            mask = cv2.inRange(hsv, np.array(bounds[0]), np.array(bounds[1]))

        if cv2.countNonZero(mask) > 5000:
            detected_type = garbage_type
            captured_frame = frame.copy()
            print(f"🗑️ Detected: {detected_type}")
            break

    cv2.imshow("Garbage Detection - Press ESC to stop", frame)
    if cv2.waitKey(1) == 27 or detected_type:
        break

cap.release()
cv2.destroyAllWindows()

# --- Save Captured Image ---
if detected_type and captured_frame is not None:
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{detected_type}_{timestamp}.jpg"
    save_path = os.path.join(save_dir, filename)
    save_path_abs = os.path.abspath(save_path)
    cv2.imwrite(save_path_abs, captured_frame)
    print(f"💾 Image saved: {save_path_abs}")

    # --- Insert into DB ---
    cursor.execute("INSERT INTO garbage_images2 (image_path, type) VALUES (%s, %s)",
                   (save_path_abs, detected_type))
    conn.commit()

    # --- Show correct sample image ---
    sample_path = sample_image_map.get(detected_type)
    if sample_path and os.path.exists(sample_path):
        img = cv2.imread(sample_path)
        if img is not None:
            resized_img = cv2.resize(img, (800, 600))  # Resize for better display
            cv2.imshow(f"Sample for {detected_type}", resized_img)
            print("🖼️ Showing sample image. Press any key to close.")
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print(f"⚠️ Cannot read image: {sample_path}")
    else:
        print(f"⚠️ Sample image not found for: {detected_type}")
else:
    print("⚠️ No garbage detected.")

cursor.close()
conn.close()
