# code by Nityanand Thakur.
'''
supported by & thankful to:
1)ipinfo.io.
2)nityanand86876 from github.com <email>:nityanandthakur@protonmail.com.
3)nnt12345 from github.com.
'''

import os
token = str(input("input auth token : "))
ip = str(input("input ip address : "))
cmd = 'curl ipinfo.io/'+ip+'/?token='+token
os.system(cmd)
