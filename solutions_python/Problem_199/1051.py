inf =  float("inf")

def flip(s):
	return ''.join(map(lambda x: '1' if x == '0' else '0', s))

def to_bin(n):
	return "{0:b}".format(n)

def to_int(s):
	return int(s, 2)
      
T = int(raw_input())
for t in xrange(T):
	S = raw_input().split()
	S, k, l= S[0], int(S[1]), len(S[0])

	# print "s,k,l: ", s,k,l

	S = ''.join(map(lambda x: '1' if x == "-" else '0', S))
	s = int(S, 2)

	is_break = False
	n = 0

	while s != 0 and not is_break:
		B = to_bin(s)
		# print "Case #%d: " % (t+1), B
		if len(B) >= k:
			B = flip(B[:k]) + B[k:]
			b = to_int(B)
			n += 1
			s = b
		else:
			b = to_int(B)
			if b == 0:
				s = b
			else:
				# print B, k
				is_break = True

	if is_break:
		print "Case #%d: IMPOSSIBLE" % (t+1)
		continue

	print "Case #%d: %d" % (t+1, n)