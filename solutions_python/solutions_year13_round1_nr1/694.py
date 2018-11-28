thefile = "A-small-attempt0"
outputfile = open(thefile+".out", "w")

with open(thefile+".in") as f:
	ff = [[int(x) for x in line.split()] for line in f]

#with open(thefile+".in") as f:
#	ff = [[x for x in line.split()] for line in f]

#	outputfile.write("Case #%i: %s\n" % (i,check(ff[pos][0],ff[pos][1],l)))

def f(r,t):
	a = 0.5*(r-0.5)
	b = (0.5*t + a ** 2) ** (0.5)
	return int(b-a)
	
for i in range(1,ff[0][0]+1):
	outputfile.write("Case #%i: %i\n" % (i,f(ff[i][0],ff[i][1])))
