t = input()
for i in range(t):
	a1 = input()
	l1 = set()
	for j in range(4):
		line = raw_input()
		if(j == a1 - 1):
			values = line.split()
			row = [int(value) for value in values]
			l1 = set(row)
	
	a2 = input()
	l2 = set()
	for j in range(4):
		line = raw_input()
		if(j == a2 - 1):
			values = line.split()
			row = [int(value) for value in values]
			l2 = set(row)
	l = l1 & l2
	if(l):
		c = list(l)
		if(len(c) == 1):
			print "Case #{0}:".format(i+1),c.pop()
		else:
			print "Case #{0}: Bad magician!".format(i+1)
	else:
		print "Case #{0}: Volunteer cheated!".format(i+1)