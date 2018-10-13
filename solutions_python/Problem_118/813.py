import math
def is_palindrome(s):
	if len(s)<=1:
		return True
	elif s[0] == s[-1]:
		return is_palindrome(s[1:-1])
	else:
		return False

def find_fns(a, b):
	ra = int(math.sqrt(a)) - 1
	rb = int(math.sqrt(b)) + 1
	count = 0
	for i in range(ra, rb+1):
		if is_palindrome(str(i)):
			p = i * i
			if a <= p <= b and is_palindrome(str(p)):
				count += 1
	return count

t = int(raw_input())
for i in range(0, t):
	a, b = [int(x) for x in raw_input().split()]
	count = find_fns(a, b)
	print 'Case #%s: %s' % (i+1, count)
