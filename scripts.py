import os

email = input("email = ")
rmote_username = input("username = ")
rmote_password = input("password = ")
ip_address = input("Server IP Address = ")
servername = input("Server Name = ")
ssh_port = input("New SSH port between 1050 and 45000= ")


os.system("mkdir {}".format(servername))

os.system("sed 's/<os_username>/{}/g' remote1.sh > {}/Remote1.sh".format(rmote_username,servername))

os.system("sed 's/<os_username>/{}/g' local2.sh > {}/Local2.sh".format(rmote_username,servername))
os.system("sed -i '' 's/<vps_ip_addr>/{}/g' {}/Local2.sh".format(ip_address,servername))

os.system("sed 's/<vps_ip_addr>/{}/g' remote2.sh > {}/Remote2.sh".format(ip_address,servername))
os.system("sed -i '' 's/<eamil_addr>/{}/g' {}/Remote2.sh".format(email,servername))
os.system("sed -i '' 's/<vps_name>/{}/g' {}/Remote2.sh".format(servername,servername))
os.system("sed -i '' 's/<os_username>/{}/g' {}/Remote2.sh".format(rmote_username,servername))
os.system("sed -i '' 's/<os_password>/{}/g' {}/Remote2.sh".format(rmote_password,servername))
os.system("sed -i '' 's/<defined_ssh_port>/{}/g' {}/Remote2.sh".format(ssh_port,servername))

os.system("chmod +x {}/*.sh".format(servername))

os.system("ssh root@{} 'apt-get update'".format(ip_address))

os.system('echo "{}:{}" >> .credentials'.format(rmote_username,rmote_password))


print('-----------------')
print('     Remote1     ')
print(' Please Wait...  ')
print('-----------------')

os.system("ssh root@{} 'bash -s' < ./{}/Remote1.sh".format(ip_address,servername))

print('-----------------')
print('     Local1      ')
print(' Please Wait...  ')
print('-----------------')

os.system("./{}/Local2.sh".format(servername))

print('-----------------')
print('    Remote2      ')
print(' Please Wait...  ')
print('-----------------')

os.system("ssh root@{} 'bash -s' < ./{}/Remote2.sh".format(ip_address,servername))

#os.system("ssh root@{} 'apt-get upgrade'".format(ip_address))

#TODO set up new non-root users, later disable root login

#TODO install all necessary programs

print('---------------------------------')
print('       Finished installing       ')
print(' Firewalld, nginx, fail2ban, ntp ')
print('---------------------------------')

#new_user=input("Do you want to add another user to the server: [Y]es [N]o")

#while new_user == "Y":
#    rmote_username = input("username = ")
#    rmote_password = input("password = ")

#    os.system("sed -i '' 's/<os_username>/{}/g' {}/Remote1.sh".format(rmote_username,servername))

#    os.system("sed -i '' 's/<os_username>/{}/g' {}/Local2.sh".format(rmote_username,servername))
#    os.system("sed -i '' 's/<vps_ip_addr>/{}/g' {}/Local2.sh".format(ip_address,servername))

#    os.system('echo "{}:{}" >> .credentials'.format(rmote_username,rmote_password))

os.system('ssh -p {} {}@{} "bash -s" < sudo apt-get install python-pip tree'.format(ssh_port,rmote_username,ip_address))

github_clone=input("Enter a github link to clone: ")
os.system('ssh -p {} {}@{} "bash -s" < git clone {}'.format(ssh_port,rmote_username,ip_address,github_clone))
