from flask import Flask, render_template, request, url_for, redirect, send_file, make_response, jsonify
# import mysql.connector
# from mysql.connector import Error

from mysql.connector import MySQLConnection, Error
import mysql.connector
from python_mysql_dbconfig import read_db_config

from graph import survey_data, survey_analysis_01, survey_analysis_02, close_connection

import logging

from flask_caching import Cache

import time


app = Flask(__name__)
application = app # our hosting requires application in passenger_wsgi
cache = Cache(app, config={'CACHE_TYPE': 'null'})

def mycache():
    cache.init_app(app, config={'CACHE_TYPE': 'null'})

    with app.app_context():
        cache.clear()

app.config["CACHE_TYPE"] = "null"
cache.init_app(app)

app.debug = True


db_config = read_db_config()
conn = None
conn = MySQLConnection(**db_config)


@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.route('/')
def home():
   # """Default route"""
   # app.logger.debug('this is a DEBUG message')
   # app.logger.info('this is an INFO message')
   # app.logger.warning('this is a WARNING message')
   # app.logger.error('this is an ERROR message')
   # app.logger.critical('this is a CRITICAL message')

   return render_template('survey.html')

# @app.route('/covid19_survey')
# def new_survey():
#    return render_template('survey.html')

# @app.route('/covid19_survey')
# def new_survey1():
#    return render_template('survey copy.html')


# @app.route('/addrec',methods = ['POST', 'GET'])
# def addrec():
#    if request.method == 'POST':     
#       try:
#          urname = request.form['urname']
#          email = request.form['email']
#          age = request.form['age']
#          profession = request.form['profession']
#          question1 = request.form['question1']
#          question2 = request.form['question2']
#          question3 = request.form['question3']
#          question4 = request.form['question4']
#          question5 = request.form['question5']
#          question6 = request.form['question6']
#          question7 = request.form['question7']
#          question8 = request.form['question8']
#          question9 = request.form['question9']
#          question10 = request.form['question10']
         
#          cursor = conn.cursor()
#          cursor.execute("SET AUTOCOMMIT = 1")
#          cursor.execute("INSERT INTO covid19_survey (Name,Email,Age,Profession,Question1,Question2,Question3,Question4,Question5,Question6,Question7,Question8,Question9,Question10) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(urname, email, age, profession, question1, question2, question3, question4, question5, question6, question7, question8, question9, question10))
#          conn.commit()
#          msg = " Thanks for your time!! Your answers have been successfully received by us."
#          survey_data()
#          survey_analysis_01()
#          survey_analysis_02()
#          print ("Success")
#          # time.sleep(1)

#       # except mysql.connector.IntegrityError as err:
#       except Exception as err:
#          print("Error: {}".format(err))
#          print ("Exception - Something went wrong.")
#          conn.rollback()
#          msg = "Something went wrong. Please try again."

            
#       finally:
#          urname = request.form['urname']
#          cursor.execute("select * from covid19_survey where Name= %s", (urname,))
#          data = cursor.fetchall()
#          return render_template("result.html", msg = msg ,data = data)
#          # conn.close()
#          # cursor.close()
#    return render_template("home.html")

# def func1():
#     pass


@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':     
      try:
         urname = request.form['urname']
         email = request.form['email']
         age = request.form['age']
         profession = request.form['profession']
         question1 = request.form['question1']
         question2 = request.form['question2']
         question3 = request.form['question3']
         question4 = request.form['question4']
         question5 = request.form['question5']
         question6 = request.form['question6']
         question7 = request.form['question7']
         question8 = request.form['question8']
         question9 = request.form['question9']
         question10 = request.form['question10']
         
         cursor = conn.cursor()
         cursor.execute("SET AUTOCOMMIT = 1")
         #cursor.execute("INSERT INTO covid19_survey (Name,Email,Age,Profession,Question1,Question2,Question3,Question4) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(urname, email, age, profession, question1, question2, question3, question4))
         cursor.execute("INSERT INTO covid19_survey (Name,Email,Age,Profession,Question1,Question2,Question3,Question4,Question5,Question6,Question7,Question8,Question9,Question10) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(urname, email, age, profession, question1, question2, question3, question4, question5, question6, question7, question8, question9, question10))
         conn.commit()
         msg = " Thanks for your time!! Your answers have been successfully received by us."
         survey_data()
         survey_analysis_01()
         survey_analysis_02()
         print ("Success")
         # time.sleep(1)

      # except mysql.connector.IntegrityError as err:
      except Exception as err:
         print("Error: {}".format(err))
         print ("Exception - Something went wrong.")
         conn.rollback()
         msg = "Something went wrong. Please try again."

            
      finally:
         urname = request.form['urname']
         cursor.execute("select * from covid19_survey where Name= %s", (urname,))
         data = cursor.fetchall()
         return render_template("result.html", msg = msg ,data = data)
         # conn.close()
         # cursor.close()
   return render_template("survey.html")

# def func2():
#     pass
# # Not in use
# @app.route('/user_name')
# def user_name():
#    return render_template('user_name.html')

# # Not in use
# @app.route('/user_report',methods = ['POST', 'GET'])
# def user_report():
#    if request.method == 'POST':
#        try:
#           email = request.form['email']
#           cursor = conn.cursor()
#           cursor.execute("COMMIT")
#           cursor.execute("select * from covid19_survey where email= %s", (email,))
#           #data = cursor.fetchall()

#        except:
#           conn.rollback()
#           msg = "Error in Retrivel"
      
#        finally:
#            data = cursor.fetchall()
#            if cursor.rowcount != 0:
#               return render_template("user_report.html",data = data)
#            else:
#               msg = "Invalid Number."
#               msg2 = "Please enter the number which you provided at the time of survey."
#               return render_template("user_report_none.html",msg = msg, msg2 = msg2)
#    return render_template("user_report.html",data = data)

# Report Listing - For Admin
@app.route('/findme')
def list():
   cursor = conn.cursor()
   cursor.execute("COMMIT")
   cursor.execute("select * from covid19_survey")
   data = cursor.fetchall()
   return render_template("list.html", data = data)
   conn.close()
   cursor.close()
   close_connection()


@app.route('/graph', methods=["GET"])
def graph():
   #  survey_data()
   #  bytes_obj = survey_analysis_01()
    
   #  return send_file(bytes_obj,
   #                   attachment_filename='plot.png',
   #                   mimetype='image/png')

   # return render_template("user_report.html", image=bytes_obj)
   return render_template("survey_graph.html")


# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)











@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404





if __name__ == '__main__':
   mycache()
   app.run(debug=False)
   close_connection()
