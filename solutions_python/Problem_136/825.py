import sys


def solve(t, r, c,f,x):
	i =0
	t = 0
	while t+c/(r+i*f)+x/(r+(i+1)*f) <= t+x/(r+i*f):
		#print t, r+i*f
		t += c/(r+i*f)
		i+=1
	return t+x/(r+i*f)




N = int(sys.stdin.readline().strip())
for t in range(N):
	#print "Problem", t+1
	line = sys.stdin.readline().strip()
	c, f, x = [float(v) for v in line.split(" ")]
	#print c,f, x

	#print solve(0, 2, c ,f ,x)
	print "Case #{0}: {1:0.7f}".format(t+1, solve(0, 2, c ,f ,x))
	#print "Case #{0}: {1:0.7f}".format(t+1, solve(0, 2, c ,f ,x))