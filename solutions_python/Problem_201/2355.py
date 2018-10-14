import math

def main(n, k):
	buf = [n]
	while True:
		# print buf
		# print k
		if k > len(buf):
			# print "next"
			k -= len(buf)
		else:
			buf.sort(reverse=True)
			# print "sorted buf: {}".format(buf)
			# print buf[k-1]
			return ((buf[k-1]-1)//2, buf[k-1]//2)
		# print("next2")
		buf_ = []
		for e in buf:
			buf_.extend([(e-1)//2, e//2])
		buf = buf_

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
	n, k = [int(x) for x in raw_input().split(' ')]
	minres, maxres = main(n,k)
	print "Case #{}: {} {}".format(i, maxres, minres)