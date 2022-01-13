import requests
import os
import time
from datetime import datetime

## Send a GET request to a healthcheck endpoint waiting for a 200 response
## If it is different than 200, then trigger the alert
try:
    while 1>0:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Execution time: ", current_time)
        r = requests.get("http://www.url-example.com")
        print(r.status_code)
        if r.status_code!=200:
            print("ERROR")
            for x in range(7):
                os.system('afplay /System/Library/Sounds/Sosumi.aiff')
                os.system('say "There is an error"')
                time.sleep(3)
        else:
            print("It's working fine")
        time.sleep(1200)
except requests.ConnectionError:
    print("failed to connect")