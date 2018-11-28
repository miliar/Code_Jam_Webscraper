from sys import *

lines = stdin.read().replace('\r',"").split('\n')
ntests = int(lines.pop(0))

for testno in range(1,ntests+1):
	t = 0
	c,f,x = tuple(map(float,lines.pop(0).split(' ')))
	r = 2
	times = []
	while 1:
		times.append(t+x/r)
		t += c/r
		r += f
		if len(times)>1 and times[-1]>times[-2]: break
		if t>=times[0]: break
	print "Case #"+str(testno)+":", min(times)