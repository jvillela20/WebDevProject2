# BlockBuster Film Review — Django Project

## Setup Instructions

1. Open in GitHub Codespace or clone locally
2. Install dependencies:
      pip install django
3. Navigate to the project folder:
      cd Project
4. Run migrations:
      python manage.py migrate
5. Load sample data:
      python manage.py loaddata app/fixtures/initial_data.json
6. Create a superuser (to access admin):
      python manage.py createsuperuser
7. Run the server:
      python manage.py runserver
8. Visit http://127.0.0.1:8000

Admin panel: http://127.0.0.1:8000/admin
