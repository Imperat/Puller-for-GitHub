import json
import requests
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth1

owner = 'gd'
repos = 'gridlibrary'
urlRepo = 'https://api.github.com/repos/%s/%s/pulls' % (owner, repos)
urlAuth = 'https://api.github.com/authorizations'

myAuth = OAuth1("Imperat", "6c5d0ef4bfe9ed498d17bfc2c96e73f79149643e")
myAuth2= ("Imperat", "2580258v")
myAuth3= OAuth1("Imperat", "2580258v")


r1 = requests.get(urlAuth, auth=myAuth2)

#for i in eval(r.text).items():
#    print i

print r1

r2 = requests.get(urlRepo, auth=myAuth3)
r2 = requests.get('https://api.github.com/repos/django/django/pulls')



#----------------------------------------------------------------------------
# Generate new id's list

res = json.loads(r2.text)


NewIdLists = [ i["id"] for i in res]
print NewIdLists

#----------------------------------------------------------------------------
OldIdLists = []
with open ("list_ids.txt", "r") as f:
    OldIdLists = f.readlines()
    OldIdLists = map(int, OldIdLists)

print "Tyype"
print type(OldIdLists[0])

diff = set(NewIdLists) - set(OldIdLists)

if diff: #If there are new id's
    pass
    #writeinfiles
    with open("list_ids.txt", "a") as f:
        for i in diff:
            f.write(str(i) + "\n")
else:
    pass

print "diff is" + str(diff)
