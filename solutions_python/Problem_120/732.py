import math

input_file = open('A-small-attempt0.in')

def qForm(a,b,c):
	return (-b+math.sqrt(b**2-4*a*c))/(2.0*a)

countlines = 0
for line in input_file:
	if countlines == 0:
		numOfCases = int(line)
		countlines+=1
		continue
	r,t = line.split(" ")
	r = int(r)
	t = int(t)
	a = 2
	b = (2*r-1)
	c = -t
	answer = int(qForm(a,b,c))

	print "Case #" + str(countlines) + ": " + str(answer)
	countlines+=1

