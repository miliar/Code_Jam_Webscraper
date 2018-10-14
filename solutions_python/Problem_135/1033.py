def do_trick(inf):
	first = []
	second = []
	r1 = int(inf.readline())
	for i in xrange(1, 5):
		s = inf.readline().strip()
		if (i == r1):
			first += s.split()
	r2 = int(inf.readline())
	for i in xrange(1, 5):
		s = inf.readline().strip()
		if (i == r2):
			second += s.split()
	res = set(first) & set(second)
	if len(res) == 1:
		return list(res)[0]
	elif len(res) == 0:
		return "Volunteer cheated!"
	else:
		return "Bad magician!"


inf = open("in.txt", 'r')
t = int(inf.readline())
res = ""
for i in xrange(0, t):
	res += "Case #" + str(i + 1) + ": " + do_trick(inf) + "\n"
outf = open("out.txt", 'w')
outf.write(res)
outf.close()
	
			
