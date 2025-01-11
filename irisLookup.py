import requests
print("  ")
print("discoveryOps: Iris Username Lookup")
print(" ")
print("Created by Gabriel H. @weekndr_sec")
print("https://github.com/ndr-repo")
print(" ")
print(" 'Knowledge is powerful, be careful how you use it!' ")
print(" ")
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
targetUser = input("Enter the target username: ")
print("  ")
financeUrls = {
     "https://venmo.com/u/"+targetUser,
     "https://cash.app/$"+targetUser,
     "https://revolut.me/api/web-profile/"+targetUser,
}
socialUrls = {
     "https://x.com/"+targetUser,
     "https://"+targetUser+".tumblr.com",
     "https://youtube.com/@"+targetUser,
     "https://threads.net/@"+targetUser,
     "https://rumble.com/c/"+targetUser,
     "https://instagram.com/"+targetUser
}
devUrls ={
     "https://pypi.org/user/"+targetUser,
     "https://www.npmjs.com/~"+targetUser,
     "https://github.com/"+targetUser,
     "https://hub.docker.com/v2/users/"+targetUser,
     "https://discuss.elastic.co/u/"+targetUser
     }
miscUrls ={
     "https://hackerone.com/"+targetUser,
     "https://bugcrowd.com/"+targetUser,
     "https://patreon.com/"+targetUser,
     "https://wordpress.org/support/users/"+targetUser,
     "https://soundcloud.com/"+targetUser,

}
url_content = set()
print(' ')
print('Category: Finance ')
for financeUrl in financeUrls:
    response = requests.get(financeUrl, headers=headers)
    reqUrl = response.request.url
    if response.status_code == 200:
        print(" - Profile found: ", reqUrl, end='\n')
    if response.status_code == 403: 
        print(" - Request denied by host: ", reqUrl, end='\n')
print(' ')
print('Category: Socials ')
for socialUrl in socialUrls:
    response = requests.get(socialUrl, headers=headers)
    reqUrl = response.request.url
    if response.status_code == 200:
        print(" - Profile found: ", reqUrl, end='\n')
    if response.status_code == 403: 
        print(" - Request denied by host: ", reqUrl, end='\n')
print(' ')
print('Category: Developer Sites: ')
for devUrl in devUrls:
    response = requests.get(devUrl, headers=headers)
    reqUrl = response.request.url
    if response.status_code == 200:
        print(" - Profile found: ", reqUrl, end='\n')
    if response.status_code == 403: 
        print(" - Request denied by host: ", reqUrl, end='\n')
print(' ')
print('Category: Misc: ')
for miscUrl in miscUrls:
    response = requests.get(miscUrl, headers=headers)
    reqUrl = response.request.url
    if response.status_code == 200:
        print(" - Profile found: ", reqUrl, end='\n')
    if response.status_code == 403: 
        print(" - Request denied by host: ", reqUrl, end='\n')
print(" ")
print("Scan complete.")
print(" ")
    # if response.status_code == 404:
         # print("No profile found: ", reqUrl, end='\n')