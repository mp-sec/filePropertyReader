#!usr/bin/python3

import os
import time 

userPath = input("Enter an absolute directory path: ")

with os.scandir(userPath) as dirContent:
	for entry in dirContent:
		# Filename 
		fileName = os.path.basename(entry)
		print("\tFile Name:\t", fileName)
		
		# Filepath 
		print("\tFile Path:\t", userPath)
		
		# File size 
		fileSize = fileSize = os.path.getsize(entry)
		# Get size in KB:
			# {:.2f} kilobytes".format(fileSize / 1024)
		modifiedFS = str(fileSize) + " bytes"
		print("\tFile Size:\t", modifiedFS)
		
		# Inode 
		fileInode = os.stat(entry).st_ino
		print("\tInode:\t\t", fileInode)
		
		# Last modified 
		# The return value for os.path.getmtime is equal to the number of seconds since epoch 
		# Epoch is the point when time started, which is different depending on the platform of Linux 
		# The Ubuntu epoch can be found using the code:
			# print(time.gmtime(0))
			# The above line should return the date: January 1, 1970
		fileLastModified = os.path.getmtime(entry)
		#Converts the floating point value into a readable date and time 
		modifiedFLM = time.strftime("%a, %b %d %H:%M:%S %p, %Y", time.localtime(fileLastModified))
		print("\tLast Modified:\t", modifiedFLM, "\n")
		
