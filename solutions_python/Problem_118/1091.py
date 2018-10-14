def is_square(n):
	x = n**.5
	return int(x) == x

def is_palindrome(n):
	return str(n) == str(n)[::-1]

T = int(raw_input())
for i in xrange(T):
	A,B = map(int, raw_input().split())
	print "Case #{0}: {1}".format(i+1, sum(1 for j in xrange(A,B+1) if is_square(j) and is_palindrome(j) and is_palindrome(int(j**.5))))
