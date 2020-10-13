#! python3
import smtplib
import datetime
import pickle
from getip import getipv6
from email.mime.text import MIMEText
from user import myemaill, mysec, emailsend, emailsendCJ

emailsmtp = "smtp.office365.com"
emailport = 587
data = r'C:\Users\Callerin\Python\TaskSchedule\data.pk'
ipchange = False
# emailsec = "STARTTLS"

# 服务器名称: outlook.office365.com
# 端口: 993
# 加密方法: TLS
ipv6 = getipv6()
datetime = datetime.datetime.now()

try:
    file = open(data, 'rb+')
    data_before = pickle.load(file)
    file.close()
except Exception:
    data_before = ['null']
for ip in ipv6:
    if ip not in data_before:
        ipchange = True
        with open(data, 'wb') as file:
            pickle.dump(ipv6, file)
        file.close()
        break

# print(ipv6)
if ipchange:
    emailbodyIP = '\n%s\n%s\n%s\nSend By Python' % (ipv6[0], ipv6[1], datetime)

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
