import mysql.connector

covid19db_new = mysql.connector.connect(
 host="[Replace me with mysql server host ip]",
 user="[Replace me with mysql username]",
 password="[Replace me with mysql password]"
)

cursor = covid19db_new.cursor()

# Create Database

def create_db(dbname):
        cursor.execute("SHOW DATABASES LIKE 'covid19_survey_dev'")
        database = cursor.fetchall()

        if database !=  [('covid19_survey_dev',)]:
            cursor.execute("CREATE DATABASE IF NOT EXISTS covid19_survey_dev")
            print ("Created database successfully")

            cursor.execute("SHOW DATABASES LIKE 'covid19_survey_dev'")
            db_check = cursor.fetchall()
            print(db_check)
            
        else:
            print("DB covid19_survey_dev already Exists.")
            cursor.execute("SHOW DATABASES LIKE 'covid19_survey_dev'")
            db_check = cursor.fetchall()
            print("DB is:", db_check)
        
def create_table():
    try:
        cursor.execute('USE covid19_survey_dev')
        cursor.execute('CREATE TABLE covid19_survey (Name VARCHAR(30), Email VARCHAR(50), Age VARCHAR(30), Profession VARCHAR(30), Question1 VARCHAR(30), Question2 VARCHAR(30), Question3 VARCHAR(30), Question4 VARCHAR(30), Question5 VARCHAR(30), Question6 VARCHAR(30), Question7 VARCHAR(30), Question8 VARCHAR(30), Question9 VARCHAR(30), Question10 VARCHAR(30))')
        
        cursor.execute("SHOW TABLES")
        table_check = cursor.fetchall()
        print("Table", table_check, "created successfully.")

        cursor.close()
    except Exception as e:
        print(e)


create_db(dbname="covid19_survey_dev")
create_table()
