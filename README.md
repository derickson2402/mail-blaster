# Email Blaster

This script sends the contents of ```message.txt``` as an email to every address in ```recipients.txt```.
Each email is sent independently so that each recipient will have their own conversation thread in your email, making it easier to keep track of which address you are talking to.
This is a fairly specific tool, but I used this while house-hunting to reach out to 30 or so rental agencies and found it worked really well!

## Install Python

You need to have Python 3 installed (macOS use [homebrew](https://brew.sh/) and ```brew install python@3.10```) (Windows install Ubuntu from the Store, or you can try installing from [Python.org](https://www.python.org/downloads/windows/)).

## Log In To EMail Account

To send mail you need access to an email account (gmail, outlook, etc.).
If you have a ```@gmail.com``` email, log in online and click your profile picture >> ```Manage your Google Account``` >> ```Security``` tab on the left >> ```App passwords```.
Generate one for ```Mail``` on whatever kind of computer you have (the device doesn't matter).
If the ```App passwords``` option isn't there, make sure you have 2FA enabled and you have ```Allow insecure apps``` turned on.
When you are done with this script, you should remove the app password.
Note this won't work for university or organization emails, you will have to reach out to IT to get an app password.

## Send The Mail

With Python installed and your app password generated, put your message into ```message.txt```, and your mailing list into ```recipients.txt```.
Each address should be on a new line.
Then in ```credentials.py``` put in your email address, message subject, and app password.
When done run:

```bash
python3 mail-blaster.py
```
