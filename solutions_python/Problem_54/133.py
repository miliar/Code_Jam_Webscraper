import fractions
import sys
import math

C = int(sys.stdin.readline())

for case in range(C):
	s = sys.stdin.readline().split()
	last = int(s[2])
	gcd = abs(last - int(s[1]))
	for ti in s[2:]:
		num = int(ti)
		gcd = fractions.gcd(gcd, abs(num-last))
		last = num
	if last%gcd == 0:
		ans = 0
	else:
		ans = gcd - last%gcd
	print "Case #%d: %d"%(case+1, ans)
