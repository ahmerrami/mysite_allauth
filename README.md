# Django project with django-allauth

This project is a minimal Django setup with **django-allauth** pre-configured for authentication.

## Quick start

1. Create and activate a virtualenv:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations and create a superuser:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. Run the server:
   ```bash
   python manage.py runserver
   ```

5. Visit:
   - Home: http://127.0.0.1:8000/
   - Allauth routes: http://127.0.0.1:8000/accounts/

## Notes

- `mysite/settings.py` uses a placeholder SECRET_KEY for development. Set `DJANGO_SECRET_KEY` env var in production.
- Customize `ACCOUNT_*` settings in `mysite/settings.py` as needed.
