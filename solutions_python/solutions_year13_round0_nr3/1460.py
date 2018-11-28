import sys
import string
import time
import math

t0 = time.clock()

def isPalindrome(number):
	char_number = str(number)
	l = len(char_number)
	for i in range(0,int(l/2)):
		if char_number[i]!=char_number[l-1-i]:
			return False
	return True
		
try:
	fileInputPointer = open(sys.argv[1], 'r')
	fileOutputPointer = open(sys.argv[2], 'w')
except IOError:
	print("\nInvalid file\n")
	quit()

numberOfCases = int(fileInputPointer.readline().replace('\n',''))
for case in range(0,numberOfCases):
	numbers = fileInputPointer.readline().replace('\n','').split(' ')
	init_number = int(numbers[0])
	end_number = int(numbers[1])
	init_square = math.ceil(math.sqrt(init_number))
	end_square = math.floor(math.sqrt(end_number))
	countFairNSquare = 0
	for i in range(init_square,end_square+1):
		if(isPalindrome(i)):
			power = i*i
			if(isPalindrome(power)):
				countFairNSquare+=1
	
	fileOutputPointer.write('Case #'+str(case+1)+": "+str(countFairNSquare)+"\n")
				
print("Time: "+str(time.clock()-t0))