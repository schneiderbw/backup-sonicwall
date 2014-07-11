backup-sonicwall
================
Original Code by: Julius Schlosburg
Made Awesome by: Ben Schneider


Description:
Simple Python script to scrape a backup from a Sonicwall SSL-VPN device's web
interface


Usage:
The script will require a csv file containing the internet addressable FQDN or IP
address, the admin username and password, the SonicWall's serial number, and the sub-
directory that you want to save the file to.

The script will flow through each line of the CSV (except the first, that will be the
header) getting the variables it needs for each device, retrieve the config file, and
save it to the folder specified in the script.  It will then, optionally, send an
e-mail to an address specified to notify them that the backup has been done.

You can also specify the amount of time that you want to keep these backups.  If you
want to keep them indefinately, simply turn the option off.

You will want to keep both the CSV file and the script secure as you will be storing
passwords in them.
