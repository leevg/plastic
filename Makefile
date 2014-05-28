MANAGE=django-admin.py

test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=plastic.settings $(MANAGE) test plastic

run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=plastic.settings $(MANAGE) runserver

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=plastic.settings $(MANAGE) syncdb --noinput

migrate:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=plastic.settings $(MANAGE) migrate
