#!/usr/bin/python

import smtplib
import credentials

msgSub  = credentials.msgSub
srvHost = credentials.srvHost
srvUser = credentials.srvUser
srvPass = credentials.srvPass

recipFileName = "recipients.txt"
msgFileName   = "message.txt"

# Open files, import the recipients list, establish smtp server
recipients = [ ]
msgText = ""
with open(msgFileName) as file:
	msgText = file.read()
with open(recipFileName) as file:
	recipients = file.read().splitlines()
# Strip out empty lines to avoid getting error on address ""
while("" in recipients):
    recipients.remove("")

# Start sending. Skip over failed messages and log them to 'failed'
print("Sending... please wait...")
failed = []
for msgRecip in recipients:
	try:
		msg = """\
From: %s
To: %s
Subject: %s

%s
""" % (srvUser, msgRecip, msgSub, msgText)
	except:
		print("Error: couldn't create message for", msgRecip)
		failed.append(msgRecip)
		continue
	try:
		srv = smtplib.SMTP(srvHost, 587)
		srv.ehlo()
		srv.starttls()
		srv.ehlo()
		srv.login(srvUser,srvPass)
	except:
		print("Error: couldn't login to send to", msgRecip)
		srv.quit()
		failed.append(msgRecip)
		continue
	try:
		srv.sendmail(srvUser, msgRecip, msg)
	except:
		print("Error: couldn't send message to", msgRecip)
		failed.append(msgRecip)
	srv.close()

if len(failed) > 0:
	print("The following addresses failed to send:")
	for recip in recipients:
		print(recip)
	exit(1)
else:
	print("Done!")
	exit(0)
