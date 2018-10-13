import math
t = int(input())
for l in range(1, t + 1):
	n=int(input())
	p=[int(x) for x in str(n)]
	
	for i in range(n,0,-1):
	
		p=[int(x) for x in str(i)]
		flag=1
		for j in range(0,len(p)-1):
			if(p[j]>p[j+1]):
		
				flag=0
				break
			
				
				
		
		if(flag==1):
			print("Case #{}: {} ".format(l,i))
			break
	
			
			
		
		
		
		
	
  
	

