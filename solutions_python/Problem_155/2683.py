#import sys
#sys.stdin = open('A-large.in','r')
#sys.stdout = open('out.txt','w')
cases=int(input())


def ovation(lis,casenum):
	#print (lis,casenum)
	iter=0
	sum=0
	count=0
	counter=0
	
	for i in lis:
		i=int(i)
		if(i>0):
			if(iter>sum):
				count+=(iter-sum)
		sum+=(i+count)
		counter+=count
		count=0
		iter+=1
	
	print("Case #"+str(casenum+1)+': '+str(counter))


for i in range(cases):
	iters=input().split()
	
	(ovation(iters[1],i))