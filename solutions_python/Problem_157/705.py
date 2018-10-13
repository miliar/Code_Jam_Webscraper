import math

def entre():
	n=int(input())
	inpute=[[] for i in range(n)]
	outpute=[[] for i in range(n)]
	for i in range(n):
		s=input()
		s=s.split()
		st=input()*int(s[1])
		inpute[i]=st
	return inpute,outpute

v=['1','-1','i','-i','j','-j','k','-k']
tb=[['1','-1','i','-i','j','-j','k','-k'],['-1','1','-i','i','-j','j','-k','k'],
['i','-i','-1','1','k','-k','-j','j'],['-i','i','1','-1','-k','k','j','-j'],
['j','-j','-k','k','-1','1','i','-i'],['-j','j','k','-k','1','-1','-i','i'],
['k','-k','j','-j','-i','i','-1','1'],['-k','k','-j','j','i','-i','1','-1']]

def pose(x,y):
	ix=v.index(x)
	iy=v.index(y)
	return tb[ix][iy]

E,S=entre()

nb=0
for T in E:
	nb+=1
	r=0
	d=0
	f=len(T)-1
	cd=T[d]
	cf=T[f]
	while d<f-1 and cd!='i':
		cd=pose(cd,T[d+1])
		d+=1
	while d<f-1 and cf!='k':
		cf=pose(T[f-1],cf)
		f-=1
	m=d+1
	cm=T[m]
	while m<f-1 :
		cm=pose(cm,T[m+1])
		m+=1
	if d<f-1 and cd=='i' and cm=='j' and cf=='k':
		print("Case #"+str(nb)+": YES")
	else:
		print("Case #"+str(nb)+": NO")
