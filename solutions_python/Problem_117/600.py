for t in xrange(input()):
	n,m = [int(x) for x in raw_input().split()]
	lawn = []
	statu = "YES"
	for ni in xrange(n):
		lawn.append([int(each_num) for each_num in raw_input().split()])
	# print lawn
	for (ni,a) in enumerate(lawn):
		for (mi,height) in enumerate(a):
			if (max([lawn[ni][mi_v] for mi_v in xrange(m)]) > height
				and max([lawn[ni_v][mi] for ni_v in xrange(n)]) > height):
				statu = "NO"
				break
		if statu == "NO": break
	print "Case #%d:"%(t+1), statu