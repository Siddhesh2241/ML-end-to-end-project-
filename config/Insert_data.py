import sys
from config.database_conn import Create_connection

from src.exception import CustomException
from src.logger import logging

def insert_student_data(gender, ethnicity, parental_education, lunch, test_preparation_course, writing_score, reading_score, results):
    connection = Create_connection()
    if connection:
        try:
          cursor = connection.cursor()
          insert_query = """
            INSERT INTO Student_score (gender, ethnicity, parental_education, lunch, test_preparation_course, writing_score, reading_score,results)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
          """
          data_tuple = (gender, ethnicity, parental_education, lunch, test_preparation_course, writing_score, reading_score, results)
          cursor.execute(insert_query, data_tuple)
          connection.commit()
          cursor.close()
          connection.close()

          logging.info("Data added into database succesfully")
        
        except Exception as e:
           raise CustomException(e,sys)