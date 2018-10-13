inputN = "B-large.in"
outputN = "output.txt"

def readInp(fileName):
	with open(fileName,'r') as inp:
		T = inp.readline()
		for i in range(int(T)):
			a = inp.readline().split()
			writeOut(outputN,i,cookieDecide(2,float(a[1]),float(a[0]),float(a[2])))

def writeOut(fileName,i,ans):
	if i==0:
		with open(fileName,'w') as out:
			out.write("Case #{0}: {1:.7f}\n".format(i+1,ans))
	else:
		with open(fileName,'a') as out:
			out.write("Case #{0}: {1:.7f}\n".format(i+1,ans))

def cookieDecide(rate,extra,farm,goal):
	time, r = 0, rate
	while (goal-farm)/r > goal / (r + extra):
		time += farm / r
		r += extra
	return time + goal/r

readInp(inputN)