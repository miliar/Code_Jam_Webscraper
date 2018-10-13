import fileinput
f = open('A-small-attempt0.in','rb')
g = open('output.txt','wb')
T = int(f.next())

for case in xrange(T):
	ans = int(f.next())
	row = [f.next().split() for i in xrange(4)]
	print row
	newans = int(f.next())
	print ans, newans
	newrow = [f.next().split() for i in xrange(4)]
	remember = row[ans - 1]
	newremember = newrow[newans - 1]
	good = set(remember) & set(newremember)
	print good, len(good)
	if len(good) == 1:
		g.write("Case #" + str(case+1) + ": " + list(good)[0] + "\n")
	elif len(good) > 1:
		g.write("Case #" + str(case+1) + ": " + "Bad magician!\n")
	else:
		g.write("Case #" + str(case+1) + ": " + "Volunteer cheated!\n")

g.close()
f.close()
