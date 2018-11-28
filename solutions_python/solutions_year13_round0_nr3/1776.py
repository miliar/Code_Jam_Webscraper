
import math

def is_palindrome(n):
	s = str(n)
	l_2 = int(len(s)/2)
	if l_2==0:
		return True
	for i in xrange(l_2):
		if s[i]!=s[-i-1]:
			return False
	return True



tcases = int(raw_input())
for d in xrange(tcases):
	bounds = map(int,raw_input().split())
	cnt = 0
	for n in xrange(1,int(math.ceil(math.sqrt(bounds[1])))+1):
		sq = n*n
		if bounds[0] <= sq <= bounds[1]:
			if is_palindrome(n) and is_palindrome(sq):
				cnt += 1
	print "Case #%d: %d" % (d+1,cnt)

