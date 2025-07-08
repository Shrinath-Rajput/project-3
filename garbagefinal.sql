use student;

CREATE TABLE garbage_images3 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    type VARCHAR(50),
    image_path VARCHAR(255)
   
);

ALTER TABLE garbage_images3 ADD COLUMN file_name VARCHAR(255);
ALTER TABLE garbage_images3 ADD COLUMN file_path VARCHAR(255);
ALTER TABLE garbage_images3 ADD COLUMN label VARCHAR(255);
ALTER TABLE garbage_images3 ADD COLUMN image VARCHAR(255);
alter table garbage_images3
 drop column image_path;

SET SQL_SAFE_UPDATES = 0;

DELETE FROM garbage_images3 WHERE image IS NULL;

SET SQL_SAFE_UPDATES = 1;


 
 alter table garbage_images3 
 drop column type;
 

select * from garbage_images3;
describe garbage_images3;

insert into garbage_images3 (file_name,file_path)values('garbageprojectimages','C:\Users\DELL\garbageprojectimages');

insert into garbage_images3 (file_name,file_path)values('garbage-dataset','C:\Users\DELL\garbageprojectimages\garbage-dataset');

insert into garbage_images3 (file_name,file_path)values('battery','C:\Users\DELL\garbageprojectimages\garbage-dataset\battery');

insert into garbage_images3 (file_name,file_path)values('biological','C:\Users\DELL\garbageprojectimages\garbage-dataset\biological');

insert into garbage_images3 (file_name,file_path)values('cardboard','C:\Users\DELL\garbageprojectimages\garbage-dataset\cardboard');

insert into garbage_images3 (file_name,file_path)values('clothes','C:\Users\DELL\garbageprojectimages\garbage-dataset\clothes');

insert into garbage_images3 (file_name,file_path)values('glass','C:\Users\DELL\garbageprojectimages\garbage-dataset\glass');

insert into garbage_images3 (file_name,file_path)values('metal','C:\Users\DELL\garbageprojectimages\garbage-dataset\metal');

insert into garbage_images3 (file_name,file_path)values('paper','C:\Users\DELL\garbageprojectimages\garbage-dataset\paper');

insert into garbage_images3 (file_name,file_path)values('plastic','C:\Users\DELL\garbageprojectimages\garbage-dataset\plastic');

insert into garbage_images3 (file_name,file_path)values('shoes','C:\Users\DELL\garbageprojectimages\garbage-dataset\shoes');

insert into garbage_images3 (file_name,file_path)values('trash','C:\Users\DELL\garbageprojectimages\garbage-dataset\trash');






