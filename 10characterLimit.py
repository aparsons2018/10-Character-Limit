#Austin Parsons
import os
f = open("input.txt") 
lines = f.readlines()
f.close()

f = open("output.txt", 'w')
for characters in lines:
	characters = characters.strip('\n')
	f.write(characters[0:10] + "\n")
	

f.close 


