# Networking
Some code to automate networking...

This code just automate the connection (by SSH) to a device and execute the commands that are needed.

In this case I used *"getpass"* like a secure action to prevent the exposition of the passwords. Its important have in mind that in Pycharm will not work correctly, and is neccesary execute it in a terminal (like cmd). It was successfully tested in Visual Studio Code.

In case that you prefeer put the password instead using getpass, you just need modify the first 13th lines like that:

import paramiko
import time
#import getpass

ssh_client =  paramiko.SSHClient()

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#password = getpass.getpass('Enter password:')

#Change the ip for the ip of your device:

router = {'hostname': '198.18.133.214' , 'port' : '22' , 'username' : 'admin', 'password': 'passwordintextplane' }


