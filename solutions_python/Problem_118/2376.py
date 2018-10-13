import sys
import math

def isSquare(num):
	sqr = math.sqrt(float(num))
	sqrInt = math.trunc(sqr)
	if sqr == sqrInt:
		if(isPalindrome(str(sqrInt))):
			return True
	return False
	
def isPalindrome(num):
	numVec = []
	length = 0
	isPal = True
	for i in num:
		numVec.append (int(i))
		length = length + 1
	j=0
	while(isPal and j<length/2):
		if numVec[j] != numVec[length-j-1]:
			isPal = False
		j = j+1
	return isPal
		

cases = int(sys.stdin.readline())
#print cases
f = open('outputP2', 'w')

for i in range(0,cases):
	count = 0;
	line = sys.stdin.readline()
	limits = [int(s) for s in line.split() if s.isdigit()]
	for j in range(limits[0],limits[1]+1):
		if isPalindrome(str(j)):
			if isSquare(str(j)):
				count = count+1
				
	
	
	f.write("Case #")
	f.write(str(i+1)),
	f.write(':'),
	f.write(' '),
	f.write(str(count))
	f.write('\n')
	#print ("Case #"),
	#sys.stdout.write(str(i)),
	#sys.stdout.write(':'),
	#sys.stdout.write(' ')
	#sys.stdout.write(str(count))
	#sys.stdout.write('\n')
	
	
f.close()