import sys, math
t = int(sys.stdin.readline())
for i in range(t):
	[c, f, x] = [float(x) for x in sys.stdin.readline().split()]
	l = int(math.ceil((f*x-f*x-2*c)/(f*c)))
	j = -1
	while True:
		if (c/(2+(j+1)*f))+(x/(2+(j+2)*f)) > (x/(2+(j+1)*f)):
			break
		j += 1
	s = 0
	for k in range(j+1):
		s += c/(2+k*f)
	s += x/(2+(j+1)*f)
	if(x < c):
		s = x/2
	print("Case #"+str(i+1)+": "+"{0:.7f}".format(s))