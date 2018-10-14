import math

def makeCookies(c,f,x,k):
	time = 0
	for i in range(0,k):
		time += c/(i*f+2)
	time += x/(k*f+2)
	return time


data = [line.strip().split() for line in open("B-large.in", 'r')]
numtests = int(data.pop(0)[0])
for elem in data:
	c = float(elem[0])
	f = float(elem[1])
	x = float(elem[2])
	k = int(math.ceil((x*f-c*f-2*c)/(c*f)))
	if k>0:
		res = makeCookies(c,f,x,k)
	else: res = x/2
	ans = '%.7f'%(res)
	print "Case #" + str(data.index(elem)+1) + ": " + str(ans)

