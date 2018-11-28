def flisttostring(l):
	ret=''
	for c in l:
		ret=ret+str(c)
	ret=str(int(ret))
	return ret
def fFill(what,list,f):
	i=f
	list.sort()
	while (i<len(what)):
		what[i]=list.pop()
		i=i+1
	return 
def fRecover(what,f,list):
	i=f
	j=0
	while(i<len(what)):
		what[i]=list[j]
		j=j+1
		i=i+1
	return
import os
dir=os.listdir('.')
fname=''
for x in dir:
	if (x.find('.in')>0):
		fname=x
f=open(fname,'r')
T=int(f.readline())
for case in range(T):
	Nstr=f.readline().rstrip();
	N=int(Nstr)
	digits=[]
	for c in Nstr:
		digits.append(int(c))
	digits.append(0)
	digits.sort()
	i=0;
	result=[]
	for x in range(len(digits)):
		result.append('0')
	while(len(digits)>1):
		j=0
		while(int(flisttostring(result))<=N):
			tDigits=list(digits)
			result[i]=tDigits.pop(j)
			fFill(result,tDigits,i+1)
			j=j+1
		digits.remove(result[i])
		digits.sort()
		i=i+1
		fRecover(result,i,digits)
	result[-1]=digits[0]
	print 'Case #'+str(case+1)+':',flisttostring(result)
