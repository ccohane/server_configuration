import os

email = input('EMAIL = ')
rmote_username = input('USERNAME = ')
remote_password = input('PASSWORD = ')
ip_address = input('SERVER IP ADDRESS = ')
server_name = input('SERVER NAME = ')
ssh_port = input('NEW SSH PORT = ')
#TODO get a github link to clone

os.system("ssh root@{} 'apt-get update'".format(ip_address))

# os.system("ssh root@{} 'apt-get upgrade'".format(ip_address))

#TODO set up a new non-root user, later disable root login

os.system('ssh root@{ip_address} "bash -s" < ./update.sh'.format(ip_address=ip_address))

#TODO install necessary programs

#TODO install pip

print('______________________')
print('    CONFIGURING....   ')
print('    PLEASE WAIT....   ')
print('______________________')

os.system("mkdir {}".format(server_name))

os.system("sed 's/<vps_ip_addr>/{}/g' generic.sh > {}/{}_config.sh".format(ip_address,server_name,server_name))
#TODO aply this to each variable

#TODO delete credentials

#TODO ssh to server