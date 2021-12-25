Description
===========
This script converts a .vcf contacts file exported from Google Contacts into a format suitable to be uploaded to a BT Digital Voice DECT landline handset via the web interface on the BT Smart Hub 2. A direct upload will silently fail due to differences in formatting of phone numbers. This allows you to rapidly add lots of existing contacts without keying all the names and numbers in manually on the phone handset. 

This script was written and tested against Pythion 3.10.1. Although substantially repurposed/rewritten the basis of this script is a [a script authored by Mario Aeby](https://github.com/emeidi/strip-images-from-apple-vcard) with a different purpose. 

Usage
=====
To directly convert an input file and write to an output vcf file: 
`python google-vcf-to-bt-hub.py input.vcf output.vcf`

or to use the CLI: 
`python google-vcf-to-bt-hub.py`

Known Issues
------------
* The Digital Voice handsets tested only supported a single home, a single work, and a single mobile number per contact; any contact with multiple numbers tagged as one of these types will only have the first one imported though this will not generate a warning
* The import method on the BT Smart Hub 2 is unable to 'update' existing contacts, so it is only possible to either 'append' new contacts or wipe the entire handset and re-import all (this is probably easiest if you keep your Google Contacts up to date)

Step by step instructions
=========================
Before you begin, wipe all phone contacts from your Digital Voice handset using the phonebook on the handset -> 'Delete All' if you want to re-import the entire phonebook rather than only append new contacts.

Google Contacts
-----------
1. Open [Google Contacts](https://contacts.google.com/) 
1. Select all contacts you wish to transfer
1. From the selection context menu (three dots) at the top select 'Export'
1. Select to export as 'vCard' 
1. Save this file as 'input.vcf' in the same directory as this script

Shell
-----
1. Switch to directory containing this script and the input.vcf file
1. `python google-vcf-to-bt-hub.py input.vcf output.vcf`

BT Smart Hub 2
--------------
1. Open the managment interface for your BT Smart Hub 2 (Typically at 192.168.1.254 or similar)
1. Click on the purple icon marked 'Phone'
1. Go to the 'Contacts' tab 
1. Under 'Import' click on 'Browse' and select output.vcf 
1. Click on 'Import' 
1. Contacts should now be automatically be synced with all DECT connected Digital Voice handsets
