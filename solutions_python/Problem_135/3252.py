
def same(a, b):
	b = set(b)
	return [aa for aa in a if aa in b]

fp = open("A-small-attempt0.in", "r");
cases = int(fp.readline())

for x in range(0, cases):
	c1 = int(fp.readline())
	l1 = []
	for y in range(0, 4):
		l1.append(fp.readline()[:-1])
	c2 = int(fp.readline())
	l2 = []
	for y in range(0, 4):
		l2.append(fp.readline()[:-1])
	
	r1 = l1[c1-1].split(' ')
	r2 = l2[c2-1].split(' ')
	sol = same(r1, r2)
	
	if (len(sol) == 1):
		print "Case #" + str(x+1) + ": " + sol[0]
	elif (len(sol) > 1):
		print "Case #" + str(x+1) + ": " + "Bad magician!"
	else:
		print "Case #" + str(x+1) + ": " + "Volunteer cheated!"

