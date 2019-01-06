import json
import os

KOFA_TELEGRAM_BOT_ENV = os.environ.get('KOFA_TELEGRAM_BOT_ENV')

with open('settings.json') as f:
    settings = json.load(f)[KOFA_TELEGRAM_BOT_ENV]

POSTGRESQL_HOST = settings['POSTGRESQL_HOST']
POSTGRESQL_PORT = settings['POSTGRESQL_PORT']
POSTGRESQL_DATABASE = settings['POSTGRESQL_DATABASE']
POSTGRESQL_USER = settings['POSTGRESQL_USER']
POSTGRESQL_PASSWORD = settings['POSTGRESQL_PASSWORD']

TELEGRAM_TOKEN = settings['TELEGRAM_TOKEN']