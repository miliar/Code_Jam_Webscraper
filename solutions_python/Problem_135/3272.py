from sets import Set

inp = 'A-small-attempt0.in'
outp = 'out.out'
f = open(inp, 'r')
g = open(outp, 'w')
t = int(f.readline())
print t

for x in range(t):
	a = Set()
	c = Set()
	z = []
	for y in range(10):
		z.append(f.readline())
	row = int(z[0])
	print row
	for b in z[row].split(' '):
		a.add(int(b))
	row2 = int(z[5])
	print row2
	for b in z[row2+5].split(' '):
		c.add(int(b))
	print a 
	print c
	d = a.intersection(c)
	if len(d) == 0:
		#liar
		g.write("Case #"+str(x+1)+": Volunteer cheated!\n")
	elif len(d) == 1:
		#this one
		g.write("Case #"+str(x+1)+": "+str(d.pop())+'\n')
	elif len(d) > 1:
		#bad magician
		g.write("Case #"+str(x+1)+": Bad magician!\n")