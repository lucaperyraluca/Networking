import paramiko
import time
import getpass

ssh_client =  paramiko.SSHClient()

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

password = getpass.getpass('Enter password:')

#Change the ip for the ip of your device, and the user:

router = {'hostname': '198.18.133.214' , 'port' : '22' , 'username' : 'admin', 'password': password }

print(f'connecting to {router["hostname"]}')


ssh_client.connect(**router, look_for_keys=False, allow_agent=False)


#The time.sleep it may be necessary change depending on the time the entered commands take

shell = ssh_client.invoke_shell()
shell.send('terminal length 0\n')
shell.send('show version\n')
shell.send('show ip interface brief\n')
time.sleep(1)

output=shell.recv(10000)
output=output.decode('utf-8')
print(output)



if ssh_client.get_transport().is_active() == True:
    ssh_client.close()
    print(f'Closing connection to {router["hostname"]}')
