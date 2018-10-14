import sys

data = [x.strip() for x in open(sys.argv[1])]

T = int(data.pop(0))

for t in xrange(T):
	N = int(data.pop(0))
	C = [long(x) for x in data.pop(0).split(" ")]
	total = 0
	for c in C:
		total = total ^ c
	if total != 0:
		print "Case #%d: NO" % (t+1)
	else:
		C.sort()
		mask = (2**len(C))-2
		while mask > 0:
			left = right = 0
			total_left = total_right = 0
			for i, v in enumerate(C):
				if (2**i) & mask:
					left = left ^ v
					total_left += v
				else:
					right = right ^ v
					total_right += v
			if left == right:
				break
			mask -= 1
		else:
			print "ERROR"
			sys.exit(1)
		print "Case #%d: %d" % (t+1, max(total_left, total_right))
