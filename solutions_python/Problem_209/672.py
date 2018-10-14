import math
lines = [line.rstrip('\n') for line in open('q1.inp')]
numOfCases=int(lines.pop(0))
for i in range(numOfCases):
	n,k=map(int,lines.pop(0).split(' '))
	rha=[]
	rhb=[]
	for j in range(n):
		a,b=map(float,lines.pop(0).split(' '))
		rha.append([a,b,a*b])
		rhb.append([a,b,a*b])
	rha.sort(key=lambda x: x[2],reverse=True)
	rhb.sort(key=lambda x: x[0],reverse=True)
	area1=0
	area2=0
	total=0
	maxrad=0
	for j in range(k):
		total+=rha[j][2]
		if maxrad<rha[j][0]:
			maxrad=rha[j][0]
	area1=maxrad*maxrad*math.pi+2*total*math.pi
	if rhb[0][0] == maxrad:
		solution="Case #"+str(i+1)+": "+str(area1)
		print solution
		continue
	total=0
	for j in range(k-1):
		total+=rha[j][2]
		if maxrad<rha[j][0]:
			maxrad=rha[j][0]
	total+=rhb[0][2]
	area2=rhb[0][0]*rhb[0][0]*math.pi+2*total*math.pi
	if area2>area1:
		solution="Case #"+str(i+1)+": "+str(area2)
	else:
		solution="Case #"+str(i+1)+": "+str(area1)
	print solution
