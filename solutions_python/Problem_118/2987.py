from math import *
import fileinput

def isPalindrome(n):
	t = n
	r = 0
	while(n > 0):
		r = r*10 + n%10
		n = n//10
	if(t == r):
		return(1)
	else:
		return(0)

fairAndSquare_memo = {}

def isFairAndSquare(n):
	if n in fairAndSquare_memo:
		return fairAndSquare_memo[n]
	if(isPalindrome(n) and modf(sqrt(n))[0] == 0 and isPalindrome(sqrt(n))):
		fairAndSquare_memo[n] = 1
		return 1
	else:
		fairAndSquare_memo[n] = 0
		return 0

def isFairAndSquareRanged(m, n):
	sum = 0
	for i in range(m, n+1):
		if(isFairAndSquare(i)):
			sum = sum + 1
	return sum


f = open("C-small-attempt0.in")
t = int(f.readline().rstrip())
for i in range(1, t+1):
    line = f.readline().rstrip().split(" ")
    print("Case #" + str(i) + ": " + str(isFairAndSquareRanged(int(line[0]), int(line[1]))))

f.close()
