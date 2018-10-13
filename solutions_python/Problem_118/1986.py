import fileinput
import sys
import math

def isPalindrome(num):
	word = str(num)
	#print(word)
	for i in range(0,len(word)):
		#print(word[i] + " === " + word[len(word)-1-i])
		if(word[i] is not word[len(word)-1-i]):
			return False
	else:
		return True

infile=fileinput.input()
numCases=int(infile.readline())

board = [[0 for x in range(4)] for x in range(4)] 
for case in range(1,numCases+1):
	sys.stdout.write("Case #"+str(case)+": ")

	line = infile.readline().strip().split()
	min=int(line[0])
	max=int(line[1])
	count=0

	for attempt in range(math.ceil(math.sqrt(min)), math.floor(math.sqrt(max)+1)):
		if isPalindrome(attempt):
			if isPalindrome(attempt*attempt):
				count+=1
	print(count)

