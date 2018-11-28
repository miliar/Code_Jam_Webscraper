def check(a,num,testcase):
	count=0
	tcount=0;
	for i in range(0,len(a)-1):
		if(a[i]>=a[i+1]):
			count=count+1
	if(len(a)-1==count):	
		return True
	else:
		return False
			
	
def mak(n):
	temp=n	
	numlist=[]
	while(temp>0):
		numlist.append(temp%10)
		temp=temp/10
	return numlist	
t=int(input())
for var in range(1,t+1):
	n=int(input())
	numlist=mak(n)
	ans=check(numlist,n,var)
	while(ans!=True):
		n=n-1
		numlist=mak(n)
		ans=check(numlist,n,var)
	print "Case #%d: %d"%(var,n)


