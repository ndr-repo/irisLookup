from curl_cffi import requests
print("  ")
print("discoveryOps: Iris Username Lookup")
print(" ")
print("Created by Gabriel H. @weekndr_sec")
print("https://github.com/ndr-repo")
print(" ")
print(" 'Knowledge is powerful, be careful how you use it!' ")
print(" ")
targetUser = input("Enter the target username: ")
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
url_content = set()
for url in urls:
    response = requests.get(url, impersonate="chrome")
    reqUrl = response.request.url
    if response.status_code == 200:
        print("Profile found: ", reqUrl, end='\n')
    if response.status_code == 403: 
        print("Request denied by host: ", reqUrl, end='\n')
print(" ")
print("Scan complete.")
print(" ")
    # if response.status_code == 404:
         # print("No profile found: ", reqUrl, end='\n')