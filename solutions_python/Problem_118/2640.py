import math

inputFile = open('C-small-attempt1.in','r')
input = inputFile.read()
num = input.split('\n')[:1]
cases = input.split('\n')[1:int(num[0])+1]

def isPalindrome(number):
	#print 'checking ... ', number
	number = str(number)
	if len(number) == 1:
		return True
	elif len(number) % 2 == 0:
		left = number[:len(number)/2]
		right = number[len(number)/2:]
	else:
		left = number[:len(number)/2]
		right = number[len(number)/2+1:]
	left = [int(i) for i in str(left)]
	right = [int(i) for i in str(right)]
	left.sort()
	right.sort()
	if left == right:
		return True
	else:
		return False




f = open('output.txt', 'r+')

for c in xrange(0,len(cases),1):
	
	numCases = 0
	results = []
	cases[c] = cases[c].split(' ')
	print cases[c]
	low = int(math.ceil(math.sqrt(float(cases[c][0]))))
	high = int(math.floor(math.sqrt(float(cases[c][1]))))
	
	for i in xrange(int(low),int(high)+1,1):
		#print i
		if isPalindrome(i) and isPalindrome(i**2):
			numCases +=1
			results.append([i,i**2])
	writestring = 'Case #' + str(c+1) +': ' +str(numCases) + '\n'
	f.write(writestring)


	
	

	