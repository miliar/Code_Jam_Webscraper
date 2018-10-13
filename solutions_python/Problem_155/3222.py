

a=input()
for k in range(a):
	smax=raw_input().split()
	level=[]
	smax.pop(0)
	tmp =0
	
	sayac=0
	for i in range(len(smax[0])):
		level.append(int(smax[0][i]))
		
	
	
	for i in range(len(level)):
		if i>0:
			tmp += level[i-1]
			if tmp<i and level[i]!=0:
				sayac+=i-tmp
				tmp+=i-tmp
		else:
			if(level[0]==0):
				tmp+=1
				sayac+=1
			else:
				tmp+=0
				sayac+=0
		
		
	print "Case #" + str(k+1) +": " +str(sayac)	
		
		
		
		
		
		
		
		
