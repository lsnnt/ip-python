import os
token = str(input("input your token from host.io : "))
web = str(input("input website address in format 'example.com' : "))
cmd = 'curl https://host.io/api/full/'+web+'?token='+token
os.system(cmd)