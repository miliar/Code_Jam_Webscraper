## Note that this is a solution to only the small case.
## The small case can be completely enumerated with relative ease
## The number of blocks for x as 1,2,3,4 is 1,1,2,5 respectively
## The number of unique (exclude symmetry) rxc boards is 10
## Thus we only need to consider a reduced number of cases, and for the
## symmetric r,c = c,r cases we output similar results
## The process of determining whether RICHARD could win, simply went
## through all the possible x-ominos that could be played by RICHARD
## and seek a viable tiling by GABRIEL

f = file('D-small-attempt0.in','r')

lines = f.readlines()
T = int(lines[0].strip())

def check_2(r,c):
	if r == 4 or c == 4:
		return "GABRIEL"
	if r == 2 or c == 2:
		return "GABRIEL"
	return "RICHARD"

def check_3(r,c):
	if r == 3 and c != 1:
		return "GABRIEL"
	if c == 3 and r != 1:
		return "GABRIEL"
	return "RICHARD"

def check_4(r,c):
	if r == 4 and c in [3,4]:
		return "GABRIEL"
	if c == 4 and r in [3,4]:
		return "GABRIEL"
	return "RICHARD"

def run(x,r,c):
	if x == 1:
		return "GABRIEL"
	if x == 2:
		return check_2(r,c)
	if x == 3:
		return check_3(r,c)
	return check_4(r,c)

for i in xrange(1,T+1):
	a = [int(j) for j in lines[i].strip().split(' ')]
	x,r,c = a
	out = run(x,r,c)
	print "Case #" + str(i) + ": " + str(out)
