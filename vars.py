#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "29378064"))
API_HASH = environ.get("API_HASH", "44cf2bea8cbe0ec4e383427aab3fa934")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
OWNER = int(environ.get("OWNER", "7572064803"))
CREDIT = "『ᛕꪖꪶᛕﺃ  ༗』"
AUTH_USER = os.environ.get('AUTH_USERS', '7572064803,1282288388').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
