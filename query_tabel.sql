create database if not exists student;

use student;

create table Student_score(
     id int primary key auto_increment,
     gender varchar(10),
     ethnicity varchar(20),
     parental_education varchar(50),
     lunch varchar(20),
     test_preparation_course varchar(20),
     writing_score int,
     reading_score int,
     Predicted_result int
     );
     
ALTER TABLE student_score ADD COLUMN Predicted_result VARCHAR(255);

ALTER TABLE student_score CHANGE COLUMN Predicted_result results VARCHAR(255);

select * from Student_score;
     
     