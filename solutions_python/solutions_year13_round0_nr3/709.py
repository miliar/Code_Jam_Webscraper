import sys
import math

def isPalindrome(n):
	ll = []
	while n > 0:
		ll.append(n%10)
		n = n - (n % 10)
		n = n / 10
	t = len(ll)
	for i in range(0, t):
		if ll[i] != ll[t-1-i]:
			return False
	return True

def go(fname='1toy.txt',verbose=False):
	f = open(fname)
	lines = [line.strip() for line in f.readlines()]
	nn = int(lines[0])
	for i in range(0, nn):
		ab = str.split(lines[i+1],' ')
		a, b = int(ab[0]),int(ab[1])
		#print a, b
		#print math.sqrt(a), math.sqrt(b)
		print "Case #" + str(i+1) + ": " + str(examine2(a, b))
	f.close()

def examine2(a, b):
	v = [1, 2, 3, 11, 22, 101, 111, 121, 202, 212, 1001, 1111, 2002, 10001, 10101, 10201, 11011, 11111, 11211, 20002, 20102, 100001, 101101, 110011, 111111, 200002, 1000001, 1001001, 1002001, 1010101, 1011101, 1012101, 1100011, 1101011, 1102011, 1110111, 1111111, 2000002, 2001002]
	ct = 0
	for j in v:
		if a <= j*j and j*j <= b:
			ct = ct + 1
	return ct

def examine(a, b):
	ct = 0
	print math.log(math.sqrt(b))/math.log(10)
	for i in range(int(math.sqrt(a))-1, int(math.sqrt(b))+1):
		if isPalindrome(i) and isPalindrome(i*i) and i*i>=a and i*i<=b: 
			print i, i*i
			ct += 1
	return ct
go(fname=sys.argv[1])
