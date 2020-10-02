import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/environhub/environhub")

from app import app as application
application.secret_key = 'ENTER-YOUR-KEY-HERE'
