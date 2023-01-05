import pandas as pd
import logging
import requests
import datetime
from pathlib import Path

# logging.basicConfig(level=logging.DEBUG)
from alice_blue import *


class account:
    def login(username, password, twoFA, api_secret, app_id):
        try:
            access_token = AliceBlue.login_and_get_sessionID(username=username,password=password,twoFA=twoFA, api_secret=api_secret,app_id=app_id)
            print(access_token)
            alice = AliceBlue(username=username, password=password, access_token=access_token)
            print (alice.get_profile())
            response = alice.get_profile()
            # response["status"] = 1
            # response["account_balance"] = 0
            print(response)
            return response
        except Exception as e:
            print(e, "none")
            return e