
f = open('B-large.in', 'r')

numTest = int(f.readline())

for i in range(numTest):
	line = f.readline().split(' ')

	x = 0
	N = int(line[0])
	S = int(line[1])
	p = int(line[2])

	sum = 0

	for j in range(3,3+N):
		#print line[j]
		n = int(line[j])
		if (n +2)/3 >= p:
			sum += 1
		elif (n + 2)/3 == p -1 and S > 0 and n > 0:
			if n % 3 != 1:
				S -=1
				sum += 1


	print "Case #" + str(i + 1) + ": " + str(sum)