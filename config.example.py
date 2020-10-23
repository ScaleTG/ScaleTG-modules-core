""" Config File
This config file contains the required configuration for this bot to work.

DO NOT TRY TO EDIT THIS FILE FROM MAIN REPO
USE https://github.com/ScaleTG-modules-core instead
"""

# Core 
bot_token = '' # Obtain from t.me/BotFather
bot_username = '' # (without @) Not required, but used by default authorization app

"""Currently enabled app, there must be a matching directory name in $CWD/apps/
For every request, it is expected that only one of the following will return a response,
otherwise, the first response returned is used. 
Prioritize your apps accordingly.
"""
enabled_apps = [
    'authorization',
]