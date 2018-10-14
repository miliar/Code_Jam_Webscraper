import math
f = open("testcase.txt")
c = int(f.readline())
for l in xrange(c):
	d = f.readline().split(' ')
	N = int(d[0])
	S = int(d[1])
	p = int(d[2])
	numbers = 0
	cont = []
	for i in xrange(N):
		cont.append(int(d[i+3]))
	for i in cont:
		q = i-p
		if q < 0:
			continue
		elif math.floor(q/2) > p-2:
			numbers += 1
		elif math.floor(q/2) == p-2 and S > 0:
			S -= 1
			numbers += 1
		
	print "Case #"+str(l+1)+": "+str(numbers)
