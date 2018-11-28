T=int(input())
for i in range(0,T):
	N=int(input())
	l=raw_input().split()
	a=[0]
	mark=[]
	count=0
	for j in range(0,N):
		if(int(l[j])!=(j+1)):
			count=count+1
	print "Case #" + str(i+1) + ": " + str(count) + ".000000"
	
					
	
	
	
	
	
	
