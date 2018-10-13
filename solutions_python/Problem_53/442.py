from math import factorial

t = input()
for c in range(0, t):

	n, k = [int(v) for v in raw_input().split(' ')]

	s = 0
	for i in range(0, k):
		s += 1
		if bin(s)[2:] == '1'+('0'*n):
			s = 0

	if bin(s)[2:] == ('1'*n):
		print "Case #%d: ON" % (c+1, )
	else:
		print "Case #%d: OFF" % (c+1, )


