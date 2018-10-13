import sys

T = int(raw_input())

for re in range(1, T + 1):
	A, B = map(int, raw_input().split())
	ans = 0
	for i in range(A, B):
		s = str(i)
		
		while(True):
			s = s[-1] + s[:-1]
			if int(s) > i and int(s) <= B:
				ans += 1
			if int(s) == i:
				break;
	print "Case #%d: %d"%(re, ans)


