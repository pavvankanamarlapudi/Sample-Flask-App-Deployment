# Heroku-Flask-Deploy
Deployement Flask App in heroku:
-------------------------------

Mandatory Files:
--------------
Procfile
requirements.txt
app.py

Deployment steps:
--------------
Create app in heroku
Move the project files from local to GitHub repository
From Heroku, connect to the same Git remote repository wehre you're project files
Enable Automatic Deployment (If you want) (or) Manual Deployement
Let's complete the build process
Take the domain and navigate to see the application result.

From CLI:
-------
Download and install the Heroku CLI.
$ heroku login

Create a new Git repository
Initialize a git repository in a new or existing directory

$ cd my-project/
$ git init
$ heroku git:remote -a <appname>

Deploy your application
Commit your code to the repository and deploy it to Heroku using Git.

$ git add .
$ git commit -am "make it better"
$ git push heroku master
