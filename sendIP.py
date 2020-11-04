#! python3
import smtplib
import datetime
import json
from getip import getipv6
from email.mime.text import MIMEText
from user import myemaill, mysec, emailsend, emailsendCJ

emailsmtp = "smtp.office365.com"
emailport = 587
data = r'D:\Data\User\Python\TaskSchedule\data.json'
ipchange = False
RunCount = 123

# emailsec = "STARTTLS"

# 服务器名称: outlook.office365.com
# 端口: 993
# 加密方法: TLS
ipv6 = getipv6()
datetime = datetime.datetime.now()
dataS ={'ip':ipv6,'RunCount': RunCount}
try:
	with open(data, 'r+') as f:
		data_before = json.load(f)
except Exception:
	data_before = {'ip': [ ]}
# with open(data, 'w+') as file:
#     file.write(json.dumps(dataS))
# file.close()

ip_before = data_before['ip']
for ip in ipv6:
	if ip not in ip_before:
		ipchange = True
		with open(data, 'w+') as file:
			file.write(json.dumps(dataS, indent=4))
		break

# print(ipv6)
if ipchange:
	emailbodyIP = '\n%s\n\n%s\nSend By Python' % (ipv6[0], datetime)

	msg = MIMEText(emailbodyIP, 'plain', 'utf-8')
	msg['Subject'] = 'IP Address'
	msg['From'] = myemaill
	msg['to'] = emailsend
	msg['Accept-Language'] = 'zh-CN'

	smtpobj = smtplib.SMTP(emailsmtp, emailport)
	smtpobj.ehlo()
	smtpobj.starttls()
	smtpobj.login(myemaill, mysec)
	print('正在发送邮件...')
	smtpobj.sendmail(myemaill, emailsend, msg.as_string())
	smtpobj.quit()
	print('已发送完成')
