infile = open('B-small-attempt0.in')
ofile = open('result2.txt','w')
line = infile.readline()
line = line.strip('\n')
T = int(line)
for kth in range(T):
	line = infile.readline().strip('\n')
	items = line.split(' ')
	a = int(items[0])
	b = int(items[1])
	k = int(items[2])
	s = 0
	for i in range(a):
		for j in range(b):
			if i&j < k:
				s += 1
	ofile.write('Case #%d: %d\n' % (kth+1, s))