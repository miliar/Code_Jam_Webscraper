import math

N = int( raw_input().strip() )

def isPalindrome(x) :
	return str(x) == str(x)[::-1]

for i in xrange(N) :
	A, B = map( long, raw_input().split(" ") )
	cnt = 0

	s = long( math.ceil( math.sqrt(A) ) )
	e = long( math.floor( math.sqrt(B) ) )
	for k in xrange(s, e+1) :
		if isPalindrome(k) and isPalindrome(k*k) :
			cnt += 1

	print "Case #" + str(i+1) + ": " + str(cnt)