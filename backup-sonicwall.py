# backup-sonicwall.py
# 2011 Julius Schlosburg
#
# Script to log on to the Sonicwall SSL-VPN and grab the settings file.

import urllib
import urllib2
import cookielib
import sys

# Change these accordingly. You must change these or the script will fail
username = 'admin_username'
passwd = 'admin_password'
filePath = '/backup/temp'
# The URL that the settings file resides at. Youre device's serial number should go at the end
settingsURL = 'https://<ssl-vpn_2000_hostname>/cgi-bin/exportConfigFile/sslvpnSettings-<device_serial.zip';

# the login page gives the necessary cookie to download the settings file
loginURL = 'https://vpn.theroi.com/cgi-bin/userLogin'
# Appear as a regular browser
headerVals = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.1)'}

# Data to post to loginURL
dataValsInit ={'ajax' : 'true',
	'domain' : 'LocalDomain',
	'login' : 'true',
	'password' : passwd,
	'portalname' : 'VirtualOffice',
	'state' : 'login',
	'username' : username,
	'verifyCert' : 0}

# Build the opener
dataInit = urllib.urlencode(dataValsInit)
header = headerVals
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
# Build the request object by passing it the login URL, the login POST data, and the
# user agent string
req = urllib2.Request(loginURL,dataInit,header)
"""
TODO

Add error handling in case the logon fails
"""

# request the login page via POST with the data defined in dataValsInit. This will return a cookie that will
# allow the opener to reach the settings file
response = opener.open(req)
# We have the cookie, close the connection
response.close()
print 'Logged in'

# grab the settings file
req = urllib2.Request(settingsURL)
response = opener.open(req)
settingsFile = response.read()
response.close
"""
TODO

Verify that the settings file ins't empty before moving on here
"""
print 'Got settings file'
print 'saving...'
# open the specified file in write binary mode, overwriting anything that was there before
saveFile = open(filePath,'wb')
saveFile.write(settingsFile)
saveFile.close
print 'settings file saved'
sys.exit()
