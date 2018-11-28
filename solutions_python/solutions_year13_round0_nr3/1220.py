import math

def isPalindrome(number, base):

	forward = number
 	reverse = 0
 	digit = 0

	while number > 0:
	 
	 	digit = number % base
	  	reverse = reverse * base + digit
	  	number = int(number / base)
	 
	return (forward == reverse)

def NFairSquare(a, b):
	a = int(math.ceil(math.sqrt(a)))
	b = int(math.sqrt(b))
	n = 0
	for x in range(a,b+1):
		if isPalindrome(x,10):
			if isPalindrome(x*x, 10):
				n=n+1
	return n


## Main
f = open('C-small-attempt0.in')
## Read the first line 
line = f.readline()
n = int(line)
line = f.readline()
k=0
while k<n:
	r = line.split()
	print 'Case #'+ str(k+1) + ': ' + str(NFairSquare(int(r[0]),int(r[1])))
	line = f.readline()
	k=k+1
f.close()

