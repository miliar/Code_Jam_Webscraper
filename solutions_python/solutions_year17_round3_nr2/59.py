
f = open('btiny.in')
fout = open('btiny.out', 'w')
f = open('bsmall.in')
fout = open('bsmall.out', 'w')
f = open('blarge.in')
fout = open('blarge.out', 'w')

numCases = int(f.readline().strip())


def mg(ranges, i):
	print 'mg before', ranges, i
	if i == len(ranges) - 1:
		p = ranges.pop(0)
		last = ranges[-1] 
		ranges[-1] = (last[0], 1440 + p[1], p[2])
		if p[2] != last[2]:
			raise ValueError("pp")
	else:
		p = ranges.pop(i)
		ranges[i] = (p[0], ranges[i][1], p[2])
		if p[2] != ranges[i][2]:
			raise ValueError("pp2")


for numCase in range(numCases):
	print 'Case {}'.format(numCase + 1)

	ss = f.readline().strip().split(' ')
	B = int(ss[0])
	A = int(ss[1])

	# Aranges = []
	# Branges = []
	Asum = 0
	Bsum = 0

	# for i in range(B):
	# 	r = readline().strip().split(' ')[0:2]
	# 	p = (int(r[0]), int(r[1]))
	# 	Branges.append(p)
	# 	Bsum += p[1] - p[0]
	# for i in range(A):
	# 	r = readline().strip().split(' ')[0:2]
	# 	p = (int(r[0]), int(r[1]))
	# 	Aranges.append(p)
	# 	Asum += p[1] - p[0]

	# Aranges.sort(key = lambda r: r[0])	
	# Branges.sort(key = lambda r: r[0])

	ranges = []
	for i in range(B):
		r = f.readline().strip().split(' ')[0:2]
		p = (int(r[0]), int(r[1]), 'B')
		ranges.append(p)
		Bsum += p[1] - p[0]
	for i in range(A):
		r = f.readline().strip().split(' ')[0:2]
		p = (int(r[0]), int(r[1]), 'A')
		ranges.append(p)
		Asum += p[1] - p[0]

	ranges.sort(key = lambda r: r[0])

	print 'range before', ranges

	while True:
		before = len(ranges)

		for person in ['A', 'B']:
			minIndex = None
			minDiff = None
			for i in range(len(ranges)):
				curR = ranges[i]
				nextR = ranges[(i+1) % len(ranges)]
				if curR[2] == person and nextR[2] == person:
					if minDiff is None or (nextR[0] - curR[1] + 1440) % 1440 < minDiff:
						minDiff = (nextR[0] - curR[1] + 1440) % 1440
						minIndex = i

			print 'minDiff', minDiff, 'sums', Asum, Bsum
			if minDiff is not None:
				if person == 'A':
					if minDiff <= 720 - Asum:
						Asum += minDiff
						mg(ranges, minIndex)
				else:
					if minDiff <= 720 - Bsum:
						Bsum += minDiff
						mg(ranges, minIndex)

		if before == len(ranges):
			break

	print 'range after', ranges
	cnt = 0
	person = ranges[-1][2]
	for i in range(0, len(ranges)):
		if person == ranges[i][2]:
			cnt += 2
		else:
			cnt += 1
			person = ranges[i][2]


	fout.write('Case #{}: '.format(numCase + 1))
	fout.write('{}\n'.format(cnt))


fout.close()

"""

Input 
 	
Output 
 
5
1 1
540 600
840 900
2 0
900 1260
180 540
1 1
1439 1440
0 1
2 2
0 1
1439 1440
1438 1439
1 2
3 4
0 10
1420 1440
90 100
550 600
900 950
100 150
1050 1400

Case #1: 2
Case #2: 4
Case #3: 2
Case #4: 4
Case #5: 6


"""

