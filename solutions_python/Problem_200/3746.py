def isTidy(n):
	if (n < 10): return True
	while n > 0:
		rd = n % 10
		n //= 10
		ld = n % 10
		if (rd < ld): return False
	return True

def left(n):
	s = str(n)
	for i in range(len(s)-1):
		if (s[i]>s[i+1]): 
			return int(s[:i+1]) * 10 ** (len(s)-i-1) - 1

def skipUntidy(n):
	if (n < 10): return n
	x = n
	while (not isTidy(x)):
		x = left(x)
	return x

T = int(raw_input())
for i in xrange(1, T+1):
	n = int(raw_input())
	result = 0
	found = False
	while (not found):
		if (isTidy(n)): 
			result = n
			found = True
			break
		n = left(n)

	print "Case #{}: {}".format(i, result)