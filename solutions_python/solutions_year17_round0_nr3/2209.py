dir="/home/yuxh/Desktop/c/c"
from math import log
def magic(n,k):
	div=2**int(log(k)/log(2))-1
	n-=div
	k-=div
	long=int(n/(div+1))
	longerdiv=n-long*(div+1)
	if k>longerdiv:
		long-=1
	if long%2==0:
		return long//2,long//2
	else:
		return (long+1)//2,long//2

	
file=open(dir)
T=int(file.readline()[:-1])
for i in range(T):
	[a,b]=file.readline()[:-1].split()
	a=int(a)
	b=int(b)
	c,d=magic(a,b)
	print("Case #"+str(i+1)+": "+str(c)+" "+str(d))
