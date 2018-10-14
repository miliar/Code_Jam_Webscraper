def palindrome(a):
	if str(a)==str(a)[::-1]:
		return True
	else:
		return False

def is_square(a):
	a=a**0.5
	return int(a)==a
	

def is_sqrtPal(a):
	return palindrome(int(a**0.5))

def check(a):
	if palindrome(a):
		if is_square(a):
			return is_sqrtPal(a)
		else:
			return False
	else:
		return False

T=int(raw_input())
for i in xrange(T):
	A,B=map(int,raw_input().split(" "))
	matching=0
	for j in xrange(A,B+1):
		if check(j):
			matching+=1
	print "Case #%d: %d" % (i+1, matching)

