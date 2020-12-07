from bs4 import BeautifulSoup as sp
import requests as req
import pandas as pd
import getpass
import json


#Ask user for Username and Password:
userName = input("Username: ")
password = getpass.getpass("Password: ")

#Configuration:
HEADERS = {'User-Agent':
	'Mozilla/5.0 (Windows NT 6.1) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
        'Accet-Language': 'en-Us, en;q=0.5'}

payload = {"Username" : "{}".format(userName),
	   "Password" : "{}".format(password),
	   "keepMeIn" : "false",
	   "TargetURL" : "https://www.specturm.net"
	  }

#URL/APIs(Not Shown)
authURL = 
billingURL =
billingStatementsAPI = 


#Request session with user auth:
session = req.session()
loginReq = session.post(url = authURL, headers = HEADERS, data = payload)

#After successful connection use api/url to retrieve data:  
data = session.get(url= billingStatementsAPI)
soup = sp(data.text, "html.parser")

print(json_billing.content)


