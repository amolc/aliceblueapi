

from pathlib import Path
import os
from datetime import datetime,timedelta

from account import account


aliceblue_username = os.environ["aliceblue_username"]
aliceblue_password = os.environ["aliceblue_password"]
aliceblue_appid = os.environ["aliceblue_appid"]
aliceblue_app_secret = os.environ["aliceblue_app_secret"]
aliceblue_twofa = os.environ["aliceblue_twofa"]

response = account.login(
    aliceblue_username, aliceblue_password, aliceblue_twofa, api_secret=aliceblue_app_secret, app_id=aliceblue_appid
)

print(account)