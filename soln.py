import os
import paramiko

import yaml

#with open('/home/afour/test.yaml', 'rw') as file:
file = open("test.yaml")
parsed_file = yaml.load(file, Loader=yaml.FullLoader)
# print(parsed_file["filenames"])
keywords1 = parsed_file["filenames"]
hostname1 = str(parsed_file["hostname"])
username1 = str(parsed_file["username"])
password1 = str(parsed_file["password"])

#hostname = "testserver.afourtech.com"
#username = "root"
#password = "test123"
# print(username, password)

#connect to remote linux m/c
ssh_client = paramiko.SSHClient()
resp = ssh_client.connect(hostname=hostname1,port=21,username=username1,password=password1)
print(resp)
#access remote linux
path ="/home" #path of the root file of server
#keywords1 = ['testfile_0', 'testfile_1', 'testfile_2']
try:
   files =  os.listdir(path)
   print(files)
   for file in files:
      print(file)
      myfile = open(file, 'rb')
      print(myfile)
      data=myfile.readlines()
      print(data)
        #path1="/file"
        #print(path1)
        #read = open(path1, 'r')
        #print(read)
      if keywords in file.read():
         os.remove(file)
except Exception as e:
   print("Not able to access directory! Error: ", e)

