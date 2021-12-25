#!/usr/bin/env python3

import sys
import os
import re

def checkArgs():
	numArgs = len(sys.argv)
	if (numArgs < 3):
		return False
	return True

def debugMsg(msg,type='Info'):
	print(type.upper() + ": " + msg)

def processPhoneNumber(phoneNumber):
    # Note that phoneNumnber should be regarded as a string
    # Replace + with 00, strip spaces and dashes
    phoneNumber = phoneNumber.replace('+','00')
    phoneNumber = phoneNumber.replace(' ','')
    phoneNumber = phoneNumber.replace('-','')
    return phoneNumber

def processFile(infile):
    cleanText = ""
    for line in infile:
        if re.match('PHOTO',line):
            debugMsg("Found line starting with PHOTO. Skipping.")
            continue 
        if re.match('EMAIL',line):
            debugMsg("Found line starting with EMAIL. Skipping.")
            continue 
        if re.match('CATEGORIES',line):
            debugMsg("Found line starting with CATEGORIES. Skipping.")
            continue 
        if re.match('\s',line):
            debugMsg("Found line starting with space. Skipping.")
            continue
        if re.match('TEL',line):
            # Need to process the phone number
            line = line.split(':')[0] + ':' + processPhoneNumber(line.split(':')[1])
        if re.match('item1.TEL',line):
            # Need to process the phone number - but change how it's stored
            # Guess that these are home numbers mostly - Google Contacts doesn't seem to put anything useful in the label field 
            line = 'TEL;TYPE=HOME:' + processPhoneNumber(line.split(':')[1])
        if re.match('item1.X-ABLabel:',line):
            debugMsg("Found label line. Skipping.")
            continue
        if re.match('item1.EMAIL',line):
            debugMsg("Found email line. Skipping.")
            continue
        cleanText += line
        
    return cleanText
    
# ===================================================================
# CLI

if checkArgs():
	# Arguments provided on command line for input and output
	filenameInput = sys.argv[1]
	filenameOutput = sys.argv[2]
else:
	filenameInput = input("Input file (.vcf): ")
	filenameOutput = input("Output file (.vcf): ")
	print("")

if not os.path.exists(filenameInput):
	debugMsg("File '" + filenameInput + "' not found",'Error')
	sys.exit(1)

if os.path.exists(filenameOutput):
	answer = input(filenameOutput + " already exists. Overwrite? (y/n)")
	if answer != 'y':
		debugMsg("Please rerun this tool and specify an output filename",'Error')
		sys.exit(1)
	else:
		print("")
	
debugMsg("Reading '" + filenameInput + "'",'Info')

infile = open(filenameInput)

clean = processFile(infile)

debugMsg("Writing " + filenameOutput)
    
outfile = open(filenameOutput,"w")
outfile.write(clean)

debugMsg("Done.")

sys.exit(0)