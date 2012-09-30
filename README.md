backup-sonicwall
================
Julius Schlosburg


Description:
Simple Python script to scrape a backup from a Sonicwall SSL-VPN device's web
interface


Usage:
You must modify the script to match your environment! You also of course should keep
it somewhere safe, as in its current form it will contain your device's username and
password.

The script will save the SSL-VPN 2000's backup file to a location you specify. 
It will overwrite the existing file, so you should grab it on some schedule with 
either your centralized backup system or something like logrotate.
