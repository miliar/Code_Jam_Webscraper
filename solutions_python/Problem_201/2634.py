def maxgapget(n,k,space,a):
	g=max(space,key = lambda x : x[0])
	#print(g)
	leftside=g[1]
	rightside=g[2]
	l=g[0]
	#print(space)
	space.remove(g);
	
	if(l%2==0):
		l=int(l/2);
		space.append((l-1,leftside,leftside+l-2))
		space.append((l,leftside+l,rightside))
		#print("even",space)
		return (l-1,l)
	else:
		l=int(l/2)+1;
		space.append((l-1,leftside,leftside+l-2))
		space.append((l-1,leftside+2,rightside))
		#print("odd",space)
		return (l-1,l-1)
x = int(input())
for v in range(x):
	n,k = map(int,input().split(" "))
	a = [0 for i in range(n+1)]
	space=[(len(a)-1,1,n)];
	
	#print(space)
	for i in range(k):
		ans=maxgapget(n,k,space,a)
	print("Case #"+"%d"%(v+1)+":",max(ans),min(ans))
	

	
