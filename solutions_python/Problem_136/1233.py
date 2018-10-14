f=open('B-large.in','r')
f2=open('Blarge.out','w')
import math
numTest=int(f.readline())

for i in range(0,numTest):
	test=f.readline().split()
	C=float(test[0])
	F=float(test[1])
	X=float(test[2])

	y=max(math.ceil(((X-C)*(2+F)-2*X)/(F*C)),0)

	time=0

	for j in range(0,y):
		time+=C/(2+j*F)

	time+=X/(2+y*F)
	f2.write("Case #"+str(i+1)+": "+str(time)+"\n")
