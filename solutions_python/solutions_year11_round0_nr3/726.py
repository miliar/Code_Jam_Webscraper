f = open("r03", "rb")
t = int(f.readline())
for i in range(t):
	f.readline()
	l = map(int, f.readline().split())
	x = reduce(lambda x,y: x^y, l)
	if (x!=0):
		print "Case #"+str(i+1)+": NO"
	else:
		c = reduce(lambda x,y:x+y, l)
		print "Case #"+str(i+1)+": "+str(c-min(l))
