import sys

def is_tidy(N):
	strN = str(N)
	lastDigit = '0'
	for x in strN:
		if lastDigit > x:
			return False
		lastDigit = x
	return True

	
T = int(raw_input())

for tc in xrange(1, T + 1):
	N = int(raw_input())
	if N > 20:
		strN = str(N)
		lastDigit = '0'
		idx = 0
		diffIdx = 0
		for x in strN:
			if lastDigit > x:
				break 

			idx += 1

			if x != lastDigit:
			   diffIdx = idx

			lastDigit = x

		if idx == len(strN):
		    ans = N
		else:	
			ans = str(int(strN[:diffIdx]) - 1) + str(10 ** (len(strN) - diffIdx) - 1)
			ans = int(ans)
	else:
		ans = N
	print "Case #%d: %d" % (tc, ans)
		

