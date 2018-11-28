import math

paralist = []
f = open('fslist')
for x in f.readlines():
	y = int(x)
	sq = int(math.floor(math.sqrt(y)))
	if str(sq) == str(sq)[::-1] :
		paralist.append(int(x))
f.close()

#print "Size = ", len(paralist)

t = int(raw_input())
#print "times =", t
for TC in range(1, t+1):
	count = 0
	c = raw_input().split()
	l = int(c[0])
	u = int(c[1])
	#print "range = ", l, u
	for j in paralist:
		if j >=l and j<= u:
			count = count +1
	print "Case #"+str(TC)+": "+str(count)