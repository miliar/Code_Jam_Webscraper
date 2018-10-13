import psyco
psyco.full()


input  = file("tris-small.in")
totalNumber = int(input.readline())
for case in range(1,totalNumber+1):
	n,m,A =  map(int,input.readline().split())
	
	#print n,m,A
	ms = []
	for x in range(n+1):
		for y in range(m+1):
			ms += [(x*y,x,y)]
	ms.sort()
	ms2 = [i[0] for i in ms]
	res = "IMPOSSIBLE"
	#print ms2
	i = 0
	j = 0
	while i< (m+1)*(n+1):
		if ms2[i] - ms2[j] < A:
			i+=1
		elif ms2[i] - ms2[j] > A:
			j+=1
		else:
			res = "0 0 %i %i %i %i" % (ms[i][1],ms[j][1],ms[j][2],ms[i][2])
					#print res
			break
	print "Case #%i: %s" %(case,res)
	

