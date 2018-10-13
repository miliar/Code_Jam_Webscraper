import sys,math
t=input()
i=0
for i in range(t):
	inp=raw_input().split()
	a=int(inp[0])
	b=int(inp[1])
	l=len(inp[0])
	final=0
	for j in range(a,b+1):
		j=int(j)
		rot=j
		tmp=[]
		for k in range(l-1):
			rot=int(j*math.pow(10,k+1)%math.pow(10,l))+int(j/math.pow(10,l-k-1))
			if b>=rot>j and rot not in tmp:
				final+=1
				tmp.append(rot)
	
	sys.stdout.write('Case #'+str(i+1)+': '+str(final)+'\n')
	
