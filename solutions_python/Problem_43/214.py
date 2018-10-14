import os
dir=os.listdir('.')
fname=''
for x in dir:
	if (x.find('.in')>0):
		fname=x
f=open(fname,'r')
T=int(f.readline())
vals=[1,0]+range(2,50)
for case in range(T):
	word=f.readline().rstrip()
	max=0
	k={}
	for c in word:
		if (not k.has_key(c)):
			k[c]=vals[max]
			max=max+1
	result=0
	for c in word:
		result=result*max
		result=result+k[c]
	print 'Case #'+str(case+1)+':',result