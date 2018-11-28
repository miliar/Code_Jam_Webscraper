import numpy

def checking(l):
	is_dot = 0
	diagonal = [[l[0][0],l[1][1],l[2][2],l[3][3]],[l[0][3],l[1][2],l[2][1],l[3][0]]]
	b = numpy.transpose(l)
	newlist = l+diagonal
	for i in range(4):
		newlist.append(b[i])
	for line in newlist:
		if '.' in line:
			is_dot = 1
		else:
			if 'X' not in line:
				return "O won"
			if 'O' not in line:
				return "X won"
	if is_dot == 1:
		return "Game has not completed"
	return "Draw"

thefile = "A-large"
outputfile=open(thefile + ".out","w")

with open(thefile+".in") as f:
	firstline = int(f.readline())
	ff = [firstline] + [list(line[:-1]) for line in f]

for i in range(1,ff[0]+1):
	l = [ff[5*i-4],ff[5*i-3],ff[5*i-2],ff[5*i-1]]
	outputfile.write("Case #%i: %s\n" % (i,checking(l)))



