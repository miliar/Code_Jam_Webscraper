import sys
sys.stdin = open("x:\\A-small-attempt0.in", "r")
sys.stdout = open("x:\\A-small-attempt0.out", "w")

for _ in xrange(input()):
	n = input()
	one = 0
	two = 0
	for i in xrange(4):
		a = map(int,raw_input().split())
		if i == n-1:
			for v in a:
				one |= 1<<v

	m = input()
	for i in xrange(4):
		a = map(int,raw_input().split())
		if i == m-1:
			for v in a:
				two |= 1<<v

	res = one & two
	print "Case #{}:".format(_+1),
	if res == 0:
		print "Volunteer cheated!"
	else:
		x = res
		bc = 0
		while x > 0:
			if (x&1) == 1:
				bc += 1
			x >>= 1
		if bc > 1:
			print "Bad magician!"
		else:
			print res.bit_length()-1
