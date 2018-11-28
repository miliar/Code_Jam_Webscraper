#from numpy import *

fin=open('A-large.in','r')
# fin=open('test.in','r')
T=int(fin.readline())

file('A-small-practice_result','w')
f=open('A-small-practice_result','w')

k=1
while k<(T+1):
	x=map(lambda x: str(x),fin.readline().split())
	smax=int(x[0])
	x=map(lambda x: int(x),x[1])

	ppl=0
	sval=0
	guests=0
	while (sval<smax)&(ppl<smax):
		if x[sval]==0:	# no audience members here
			sval+=1
		else:
			temp=ppl 	# save shyness level that is met
			ppl+=sum(x[sval:ppl+1])
			sval=temp+1
			
		if ppl<sval:	# preserve invariant ppl>=sval by adding guests
			guests=guests+(sval-ppl)
			ppl=sval

	
	f.write('Case #'+str(k)+': '+str(guests)+'\n')
	k+=1

f.close()