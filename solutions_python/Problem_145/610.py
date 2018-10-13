import math
inf = open("A-small-attempt0.in")
of = open("output.txt",'w')
t = int(inf.readline().strip('\n'))
for k in range(t):
	line = inf.readline().strip('\n')
	items = line.split('/')
	p = int(items[0])
	q = int(items[1])
	for i in range(p, 1, -1):
		if p % i == 0 and q % i == 0:
			p /= i
			q /= i
	tmp = math.log(q, 2)
	if tmp - int(tmp) != 0:
		of.write(str("Case #%d: impossible\n") % (k+1))
		print str("Case #%d: impossible") % (k+1)
		continue
	i = 0
	while p < q:
		p *= 2
		i += 1
	of.write(str("Case #%d: %d\n") % (k+1, i))
	print str("Case #%d: %d") % (k+1, i)