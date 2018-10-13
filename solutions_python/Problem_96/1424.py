import sys


f = open(sys.argv[1])
t = f.read(2)
case = 1
for i in f:
	try:
		temp = [int(j) for j in i.split(' ')]
	except:
		continue
	try:
		n, s, p = temp[0], temp[1], temp[2]
		temps = s
	except:
		continue
	scores = temp[3:]
	count = 0
	for j in scores:
		triplet = [10, 10, 10]
		c = 0
		while triplet[0] + triplet[1] + triplet[2] != j:
			triplet[c] -= 1
			c = (c + 1) % 3
		if s > 0:
			flag = 1
			for k in triplet:
				if k >= p:
					flag = 0
					break
			mi = triplet.index(max(triplet))
			mj = (mi -1 ) % 3
			if triplet[mi] < 10 and triplet[mj] > 0:
				while triplet[mi] - triplet[mj] >= 1:
					mj = (mj - 1) % 3
				while triplet[mi] - triplet[mj] >= 1:
					mi = (mj + 1) % 3
				triplet[mi] += 1
				triplet[mj] -= 1
			else:
				flag = 0
			yes = 0
			for k in triplet:
				if k >= p:
					yes = 1
			if flag == 1 and yes == 1:
				s-=1
		for k in triplet:
			if k >= p:
				count += 1
				break
	print "Case #%d: %d" % (case, count)
	case += 1