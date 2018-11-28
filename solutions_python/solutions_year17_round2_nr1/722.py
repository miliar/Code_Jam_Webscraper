import math 


fi = open('input.in','r')
wa = open('output.out','w')

test = int(fi.readline())


for i in range(1,test+1):
	distance,n=map(int,fi.readline().split())
	tempans = -1
	for x in range(0,n):
		pos,s=map(int,fi.readline().split())
		tempans = max(tempans,(distance-pos)/s)
	answer = distance/tempans
	wa.write('Case #{}: {:.6f}\n'.format(i,round(answer,6)))
fi.close()
wa.close()

