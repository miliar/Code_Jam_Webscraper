import re
import sys

if __name__=="__main__":
	fp = sys.stdin
	s = fp.readline()
	times = int(s)
	for loop in range(0 , times):
		s = fp.readline()
		s = s.split(' ')
		L = int(s[0])
		P = int(s[1])
		C = int(s[2])
		ans = 0
		while True:
			if L *C >= P:
				break
			C = C * C
			ans = ans + 1
		print "Case #%d: %d" %(loop+1, ans)
	