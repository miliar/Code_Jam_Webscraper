from sys import stdin
from math import sqrt, ceil, floor


def is_palindrome(number):
	if len(str(number)) < 2:
		return True
	reversed = int(str(number)[::-1])
	if reversed == number:
		return True
	return False	
	
		

f = open('C-small-attempt0.txt','w')
stdin = open('C-small-attempt0.in', 'r')
T = int(stdin.next().strip())
for t in xrange(1,T+1):
	A, B = map(int, stdin.next().split())
	
	sqrt_A = int(ceil(sqrt(A)))
	sqrt_B = int(floor(sqrt(B)))
	
	
	counter = 0
	
	for i in range(sqrt_A, sqrt_B+1):
		if is_palindrome(i):
			if is_palindrome(i**2):
				counter += 1
					
	#print 'Case #%d: %s' % (t, counter)	
	f.write("""Case #"""), f.write(str(t)), f.write(": "), f.write(str(counter)), f.write("\n")
	
	
f.close()	