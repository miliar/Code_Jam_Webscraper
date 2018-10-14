import string
import fractions

S = raw_input()
T = string.atoi(S)

for d in range(0,T):
	Line = raw_input()
	Line_s = Line.split()
	N = string.atoi(Line_s[0])
	Line_s.pop(0)

	for i in range(0,N):
		Line_s[i] = string.atoi(Line_s[i])

	Line_s.sort()

	pre = Line_s[0]
	mn = pre
	
	num = Line_s[1]
	g = num-pre
	mn = min(mn,num)
	pre = num

	for i in range(2,N):
		num = Line_s[i]
		g = fractions.gcd(g,num-pre)
		mn = min(mn,num)

		pre = num

	print "Case #%d: %d" % (d+1,(-mn)%g)
