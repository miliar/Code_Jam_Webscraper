import sys
import string
import math


def main():
	f=open(sys.argv[1],'r')
	times=f.readline()
	times=long(times)
	for i in range(0,times):
		x=[]
		y=[]
		ans1=f.readline()
		for j in range(0,4):
			
			x.append(f.readline().strip().split())
		
		#print ans1
		ex1=x[int(ans1)-1]
		#print ex1
		ans2=f.readline()
		for j in range(0,4):
			y.append(f.readline().strip().split())
		
		#print ans2
		ex2=y[int(ans2)-1]
		#print ex2
		xx=list(set(ex1) & set(ex2))
		#print xx
		if(len(xx)==1):
			print 'Case #' +str(i+1)+': '+str(int(xx[0]))
		elif(len(xx)==0):
			print 'Case #'+str(i+1)+': Volunteer cheated!'
		else:
			print 'Case #'+str(i+1)+': Bad magician!'
		
main()
