# Open files
inf = open('D-large.in', 'r')
outf = open('out.txt', 'w')

# Read in number of test cases
n = int(inf.readline().strip())

#Loop through test cases
for i in xrange(n):
	y = 0
	z = 0

	N = int(inf.readline().strip())
	Naomi = inf.readline().strip().split()
	Ken = inf.readline().strip().split()
	for j in xrange(N):
		Naomi[j] = float(Naomi[j])
		Ken[j] = float(Ken[j])
	Naomi = sorted(Naomi)
	Ken = sorted(Ken)

	# Deceitful War
	index = len(Ken)-1
	for j in xrange(N):
		if Naomi[j] > Ken[y]:
			y += 1
			continue
		if Ken[index-j+y] > Naomi[j]:
			continue
		else:
			y += 1

	# War
	index = 0
	for j in xrange(N):
		for k in xrange(index, N):
			if Naomi[j] < Ken[k]:
				index = k+1
				break
			index = k+1
		if index == N:
			z = N-1-j
			if Naomi[j] > Ken[N-1]:
				z += 1
			break
		
	outf.write('Case #%d: %d %d\n' % (i+1, y, z))

# Close input and output files
inf.close()
outf.close()