inf = open('b-large.in', 'r')
outf = open('FairAns.txt', 'w')

def minimize (mas, mini, mas1):
	for j in mas:
		ost = j%mini
		if ost != 0:
			mas1.append(ost)
	return None

T = int (inf.readline())
for i in xrange(T):
	print i
	c = inf.readline()
	c = map(long, c.split())
	c = c[1:]
	c.sort()
	d = []
	prev = c[0]
	for j in xrange(len(c)-1):
		if c[j+1] != c[j]:
			d.append(c[j])
	d.append(c[-1])
	c = []
	for j in d[1:]:
		sub = j-prev
		if sub != 0:
			c.append(j-prev)
	firstmin = d[0]
	minimum = min(c)
	while 1:
		if minimum != 1:
			d = c
			c = []
			minimize (d, minimum, c)
			if len(c) != 0:
				c.append(minimum)
				minimum = min(c)
			else:
				break
		else:
			break
	if minimum == 1:
		answer = 0
	else:
		if (firstmin%minimum) == 0:
			answer = 0
		else:
			answer = minimum - (firstmin%minimum)
	outf.write ('Case #' + str(i+1) + ': ' + str(answer) + '\n')
inf.close()
outf.close()

