# django-tree-menu

## Description
Django app that implements a tree-like menu with the following conditions:
* The menu is implemented using template tags.
* Everything above the selected item is expanded. The first nesting level under the selected item is also expanded.
* It is stored in database.
* Can be edited in the standart django admin panel.
* The active menu item is determined based on the URL of the current page.
* There can be several menus on one page.
* When you click on the menu, you go to the URL specified in it.

## Technologies
* Python
* Django
* HTML

## Installation and usage
Install requirements
```
pip install -r requirements.txt
```

Add your secret key to the .env file in the base directory (on the same level as manage.py)

Migrate the database
```
python manage.py makemigrations
```
```
python manage.py migrate
```
Create superuser
```
python manage.py createsuperuser
```
Run server
```
python manage.py runserver
```
