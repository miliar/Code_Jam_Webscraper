
def toggle(cake,i,flip):
	k=0;
	while(i+k < len(cake)  and k != flip):
		flipper(cake,i+k)
		k+=1;
	if(k==flip):
		return True;
	else:
		return False;
		
def flipper(cake,i):
	if(cake[i]=="+"):
		cake[i] = "-"
	else:
		cake[i] = "+"		

t=int(input())
for v in range(t):
	cake,flip = input().split(" ")
	flip= int(flip)
	cake=list(cake)
	final=0;
	i=0;
	while(i !=  len(cake)):
		if(cake[i]=="-"):
			boo=toggle(cake,i,flip)
			if(boo==False):
				final = "IMPOSSIBLE"
				break;
			else:
				final += 1;
		i+=1;
	print("Case #"+str(v+1)+":",final)
		
			
			
			
			
			
			
			
			
			
