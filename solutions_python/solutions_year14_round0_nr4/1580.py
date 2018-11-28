f = open('D-large.in','rb')
g = open('output.txt','wb')

def res(n, naomi, ken):
	pts = 0
	while len(naomi) > 0:
		if naomi[-1] > ken[-1]:
			ken = ken[1:]
			naomi = naomi[:-1]
			pts += 1
		else:
			naomi = naomi[:-1]
			ken = ken[:-1]
	return str(pts)

def res2(n, naomi, ken):
	pts = 0
	while len(naomi) > 0:
		if naomi[-1] > ken[-1]:
			pts += 1
			ken = ken[:-1]
			naomi = naomi[:-1]
		else:
			naomi = naomi[1:]
			ken = ken[:-1]
	return str(pts)
	

numCases = int(f.next())

for case in xrange(numCases):
	n = f.next()
	naomi = f.next().split()
	naomi = sorted([float(i) for i in naomi])
	ken = f.next().split()
	ken = sorted([float(i) for i in ken])
	g.write("Case #" + str(case+1) + ": " + res2(n, naomi,ken)+ " " + res(n, naomi, ken) + "\n")

f.close()
g.close()

