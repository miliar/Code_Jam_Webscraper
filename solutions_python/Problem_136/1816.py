import sys
sys.stdin = open("x:\\B-large.in", "r")
sys.stdout = open("x:\\B-large.out", "w")

for _ in xrange(input()):
	print "Case #{}:".format(_+1),
	c,f,x = map(float, raw_input().split())
	if x <= c:
		print "{:.12f}".format(x/2)
	else:
		t = 0.
		sp = 2.
		best = 100001.
		for it in xrange(999999):
			if t + x/sp <= best:
				best = t + x/sp
				t += c/sp
				sp += f
			else:
				break
		print "{:.12f}".format(best)