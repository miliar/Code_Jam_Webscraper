t = input()
for idx in xrange(1, t+ 1):

	n, k = map(int, raw_input().split())
	u = float(raw_input())
	probs =map(float, raw_input().split())

	probs.sort(reverse=True)

	max_ = -1

	for i in xrange(0, n):

		arr = probs[i:]
		s = sum(arr)
		x = (u + s)/float((n-i))
		if x >= probs[i]:
			ss = 1
			for j in xrange(0, i):
				ss *= probs[j]

			max_ = max(max_, ss*((x)**(n-i)))
	print "Case #{0}: ".format(idx) +  "%.10f" % (max_)