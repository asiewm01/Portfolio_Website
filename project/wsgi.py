import os
import sys
from django.core.wsgi import get_wsgi_application


# Add your project directory to the sys.path
project_home = '/home/Asiewm01/Portfolio_Website'
if project_home not in sys.path:
    sys.path.append(project_home)

# Set the Django settings module environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

application = get_wsgi_application()