from netmiko import ConnectHandler
import netmiko
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

Router1= {
		'device_type': 'cisco_ios',
		'ip': '192.168.177.10',
		'username': 'admin',
		'password': 'cisco',
		'secret': 'cisco',
		'verbose': False,
		}

Router2= {
		'device_type': 'cisco_ios',
		'ip': '192.168.177.20',
		'username': 'admin',
		'password': 'cisco',
		'secret': 'cisco',
		'verbose': False,
		}

#get time ping
def get_time_doing_ping():
 current_time=datetime.now()
 current_date=current_time.strftime("%d")
 current_month=current_time.strftime("%m")
 current_year=current_time.strftime("%Y")
 current_Hour=current_time.strftime("%H")
 current_Minute=current_time.strftime("%M")
 time_ping=current_Hour+":"+current_Minute+" Ngay "+current_date+" thang "+current_month+" Nam "+current_year
 return time_ping

#login and ping Doitac1 repeat 200 packets
net_connect=ConnectHandler(**Router1)
net_connect.enable()
ping_DoiTac1="**********Ping Doitac1  at "+ get_time_doing_ping()+"\n"
ping_DoiTac1+=net_connect.send_command_timing("ping 10.1.2.2 repeat 200")
ping_DoiTac1+="\n\n\n"
#print ("**********Begin ping at", get_time_doing_ping())
print(ping_DoiTac1)
print("\n\n")

#login and ping Doitac2 repeat 200 packets
net_connect=ConnectHandler(**Router2)
net_connect.enable()
ping_DoiTac2="**********Begin ping Doitac2 at "+ get_time_doing_ping()+"\n"
ping_DoiTac2+=net_connect.send_command_timing("ping 10.2.2.2 repeat 200")
print ("**********Begin ping Doitac2 at ", get_time_doing_ping())
ping_DoiTac2+="\n\n\n"
print(ping_DoiTac2)



#Thuc hien gui  mail
ket_qua_ping=ping_DoiTac1 + ping_DoiTac2
fromaddr = 'yourgmail@gmail.com'
toaddr = 'yourgmail@gmail.com'

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'BÁO CÁO PING ĐẦU NGÀY'
msg.attach(MIMEText(ket_qua_ping, 'plain'))

#Sending the email via Gmail's SMTP server on port 587
server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login("yourgmail@gmail.com", "yourpass")
server.sendmail(fromaddr, toaddr, msg.as_string())

server.quit()

