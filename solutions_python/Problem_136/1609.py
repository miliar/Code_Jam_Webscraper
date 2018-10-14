f = open('B-large.in','rb')
g = open('output3.txt','wb')
numCases = int(f.next())

def res(C, F, X):
	slope = 2
	intercept = C/slope
	time = X/slope
	slope += F
	nexttime = intercept + X/slope
	while time > nexttime:
		intercept = intercept + C/slope
		slope += F
		time = nexttime
		nexttime = intercept + X/slope
	return time


for case in xrange(numCases):
	x = f.next().split()
	g.write("Case #"+ str(case+1) + ": " + "{:.7f}".format(res(float(x[0]), float(x[1]), float(x[2])))+"\n")

g.close()
f.close()


