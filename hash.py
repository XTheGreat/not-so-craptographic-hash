#!/usr/bin/python
#======================================================================#
#                          Christianah Adigun                          #
#                          adigu002@d.umn.edu                          #

#                 MY NOT-SO-CRAPTOGRAPHIC HASH FUNCTION                #

# This program takes in input of any length from a readable file and   #
# returns a fixed length 32-bit hash as output.                        #
#======================================================================#

import sys
def chash(filename):
	# Read Input
	file = open(filename, 'r') # reads file
	inputValue = str(file.read()) # converts file input to string format
	length = len(inputValue) # compute the character length of input
	#XOR Operations
	dictionary = list(inputValue) # list to store input as an array
	if (length > 1):
		for i in range( 0 , length-1):
			asciiValue = ord(dictionary[i]) ^ ord(dictionary[i+1])
			total = int(ord(dictionary[i])) + int(ord(dictionary[i+1]))
			if(dictionary[0] == '~' or dictionary[0] == ' '): # for every file that starts with '~' or space, generate random replacement character
				dictionary[0] = chr(total%51 + 53)
		total = total + int(ord(dictionary[0])) + int(ord(dictionary[length/11]))
			
	else:
		asciiValue = ord('&')  ^ (ord('$') + ord(dictionary[0])) # if input has just one character, use '&' and '$' as Initialization Vectors
		total = int(ord('&'))  + int((ord('$')) + int(ord(dictionary[0])))

	# Processing Output Values
	outputList = list('0000')
	outputList[0] = bin((3  + (10 * (asciiValue%9+2))) * total / ord(chr(ord('*') + (total%3))) ^ ord(dictionary[0])).replace('0b', '').zfill(8) # generate first 1 to 8-bits
	outputList[1] = bin(int((total * length) ^ ord(dictionary[0]) + total)%157).replace('0b', '').zfill(8) # generate 9 to 16-bits
	outputList[2] = bin(int(asciiValue ^ total ^ length)).replace('0b', '').zfill(8) # generate 17 to 24-bits
	outputList[3]  = bin((3  + (10 * ((asciiValue + total)%9+2)))+ord(dictionary[0])/ord(chr(asciiValue%47 + 80))).replace('0b', '').zfill(8) # generate 25 to 32-bits
	
	#Display Output
	outputbinary = ''.join(map(str,outputList)) # combine all four sets of bytes to one 32-bit binary value
	binValue = outputbinary.replace('0b', '0')
	hexValue = hex(int(binValue, 2)).replace('0x', '').zfill(8)[0:8] # convert binary value to hexadecimal
	print hexValue+"  "+filename

chash(sys.argv[1])
