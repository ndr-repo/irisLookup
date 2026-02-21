import requests
import random
import sys
#
# CLI Wizard - replace var with comment:
# targetUser = input("Enter the target username: ")
#
targetUser = str(sys.argv[1]).strip()
user_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
               'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15']
for i in user_agents:
    headers = {'User-Agent': random.choice(user_agents)}
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
#
# If you want to inspect with a proxy tool (ie: mitmproxy):
# proxies = {"https": "http://localhost:8080"}
#
print("  ")
print(str("irisLookup - Username Search Tool for OSINT"))
print(" ")
print("Created by Gabriel H. @weekndr_sec")
print("https://github.com/ndr-repo")
print(" ")
print(" 'Knowledge is powerful, be careful how you use it!' ")
print(" ")
print("  ")
urls = {
     "https://venmo.com/u/"+targetUser,
     "https://cash.app/$"+targetUser,
     "https://revolut.me/api/web-profile/"+targetUser,
     "https://patreon.com/"+targetUser,
     "https://x.com/"+targetUser,
     "https://youtube.com/@"+targetUser,
     "https://threads.net/@"+targetUser,
     "https://instagram.com/"+targetUser,
     "https://hackerone.com/"+targetUser,
     "https://bugcrowd.com/"+targetUser,
     "https://github.com/"+targetUser,
     "https://hub.docker.com/v2/users/"+targetUser,
     "https://discuss.elastic.co/u/"+targetUser,
     "https://wordpress.org/support/users/"+targetUser,
     "https://"+targetUser+".tumblr.com",
     "https://soundcloud.com/"+targetUser,
     "https://rumble.com/c/"+targetUser,
     "https://pypi.org/user/"+targetUser,
     "https://www.npmjs.com/~"+targetUser
}
print(str("Target User: ") + str(targetUser))
url_content = set()
for url in urls:
    try:
        response = requests.get(url, headers=headers)
        reqUrl = response.request.url
        if response.status_code == 200:
            logging.info(str("Profile found: ") + str(reqUrl))
        if response.status_code == 403:
            logging.error(str("Request denied by host: ") + str(reqUrl))
        if response.status_code == 404:
            logging.warning(str("No profile found: ") + str(reqUrl))
    except:
        requests.exceptions.SSLError
        continue
print("Scan complete.")
