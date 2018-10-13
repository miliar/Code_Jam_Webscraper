import sys
import os

count = int(sys.stdin.readline().strip())

for i in xrange(count):
	num = sys.stdin.readline().strip()
	toks = [int(val) for val in sys.stdin.readline().strip().split(" ")]
	val = 0
	for tok in toks:
		val = val ^ tok
	if(val != 0):
		print "Case #%d: NO" % (i+1)
	else:
		toks = sorted(toks)
		sum = 0
		for v in toks[1:]:
			sum = sum + v
		print "Case #%d: %d" % (i+1,sum)