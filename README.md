## You May Encounter a Few Errors 
### When Working with Your First DJango Projection
#### And during deployment
##### This brief repo highlights some common issues and how you can fix them
###### I Hope it saves you a headache!


# Development Bugs
### Cannot find reference 'url' ; 
#### Import django.conf.urls could not be resolved; 
#### cannot import name 'url' from 'django.conf.urls'

* instead of:

`from django.conf.urls import url`

* use:

`from django.urls import re_path`

* You can then use re_path the same way you would have used url


### django.db.utils.OperationalError: no such table: auth_user

* Solution 1: 

`python3 manage.py makemigrations` or `py manage.py makemigrations`

    Next possible error: no changes detected

* Try solution 2: 

`python3 manage.py migrate` or `manage.py migrate`


### TypeError: __init__() missing 1 required positional argument: 'on_delete'

* Solution: 

In the class & line that throws the error, add a parameter `on_delete` and equate it to `models.CASCADE`, i.e:

    editor = models.ForeignKey(Editor,on_delete=models.CASCADE)

# Deployment Bugs

### 'heroku' does not appear to be a git repository

* run: 

`heroku git:remote -a yourappnamehere`

or 

`heroku git:remote -app yourappnamehere`


### '.herokuapp.com', is invalid. Must be in the format ▸ FOO=bar.

* Try removing this line in your `.env` : 

`ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'`

* Next possible error:

#### {} not found. Declare it as envvar or define a default value.'.format(option)

* In your poject's settings.py, search for & remove this line: 

`ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())`

* ... since we already deleted the allowed hosts option in `.env` 


## After successful deployment... 
### relation "news_article" does not exist 

* Follow these steps:

  * delete your local `migrations` folder 
  * run `heroku run bash`
  * run `python manage.py makemigrations`
  * run `cd yourappname`
  * run `ls` to confirm that you have a `migrations` directory 
  * run `cd migrations`
  * run `ls` to confirm that you do not have a `versions` directory 
  * run `mkdir versions`
  * run `cd versions`
  * run `touch .keep`
  * run `cd ~` (return to your root folder)
  * or, return step by step, i.e:
      * ru `cd ..` (return to migrations dir)
      * run `cd ..` (return to your app dir)
      * run `cd ..` (return to your root folder)

  * run `python manage.py migrate`
  * run `exit` (exit heroku bash)
  * run `git add .`
  * run `git commit -m "update remote migrations && redeploy"`
  * run `git push heroku master`


###### Kind regards! Happy hacking! 