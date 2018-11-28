x=int(input())
def find(ar):
	x = list(map(int,list(ar)))
	a =len(ar)
	for i in range(a-1,0,-1):
		if(x[i] < x[i-1]):
			x[i-1] = x[i-1]-1;
			x[i] = 9;
			for j in range(i+1,len(ar)):
				if(x[j] < 9):
					x[j] = 9;
				elif(x[j] == 9):
					break;
	return x; 
					
			
			
		
for i in range(x):
	l=find(input())
	le = len(l)
	for j in range(le):
		if(l[j]==0):
			l.pop(0);
		else:
			break;
	a = list(map(str,l))
	o=i+1;
	print("Case #"+str(o)+":","".join(a))
			
