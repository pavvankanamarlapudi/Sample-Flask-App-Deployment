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
Extra Tips:
Maintainence mode:
=================
If you’re deploying a large migration or need to disable access to your application for some length of time, you can use Heroku’s built in maintenance mode. It will serve a static page to all visitors, while still allowing you to run rake tasks or console commands.
heroku maintenance:on
heroku maintenance:off

if you want to shutdown the app:
==============================
heroku ps:scale web=0 --app myAppName
