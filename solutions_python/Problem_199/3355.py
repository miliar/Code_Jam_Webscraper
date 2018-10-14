
def toggle(pc,i,fl):
	def change(pc,i):
		if(pc[i]=="+"):
			pc[i] = "-"
		else:
			pc[i] = "+"	
	k=0;
	while(i+k < len(pc)  and k != fl):
		change(pc,i+k)
		k+=1;
	if(k==fl):
		return True;
	else:
		return False;

		
	

t=int(input())
for l in range(t):
	pc,fl = input().split(" ")
	fl= int(fl)
	pc=list(pc)
	total=0;
	n=0;
	while(n !=  len(pc)):
		if(pc[n]=="-"):
			boolcheck=toggle(pc,n,fl)
			if(boolcheck==False):
				total = "IMPOSSIBLE"
				break;
			else:
				total += 1;
		n+=1;
	print("Case #"+str(l+1)+":",total)
		
			
			
			
			
			
			
			
			
			
