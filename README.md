# Wagtail Django Tutorial

## How to install
```bash
$> mkdir wagtail-django
$> cd wagtail-djago
$> pipenv shell
$> pip install wagtail
$> pip freeze | grep wagtail
$> wagtail start mysite
$> mv mysite site
$> cp -r site/* .
$> rm -rf site
$> pip install -r requirements.txt
$> python manage.py migrate
$> python manage.py createsuperuser
$> python manage.py runserver
```

## Getting Started with First Home Page in Wagtail CMS

## How to install Django Debug Toolbar

## Adding Bootstrap Theme
https://bootswatch.com/superhero/

## How to add a new Wagtail Page from Scratch
1. Install a new djago app
```bash
$> python manage.py startapp flex
```

2. Add `flex` to django's INSTALLED_APPS.

3. Add some code to `flex/models.py`. 

## What is a StreamField?
Content does not need to be fixed. 