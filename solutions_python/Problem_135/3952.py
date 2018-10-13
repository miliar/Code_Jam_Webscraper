inp=open('input1','r')
out=open('out1','w')
t=int(inp.readline())
for i in range(t):
	r1=int(inp.readline())
	a=[[int(k) for k in inp.readline().split()] for j in range(4)]
	r2=int(inp.readline())
	b=[[int(k) for k in inp.readline().split()] for j in range(4)]
	count=0
	for j in range(4):
		for k in range(4):
			if(a[r1-1][j]==b[r2-1][k]):
				count+=1
				card=j
	if(count==0):
		out.write("Case #"+str(i+1)+": Volunteer cheated!\n")
	elif(count==1):
		out.write("Case #"+str(i+1)+": "+str(a[r1-1][card])+"\n")
	else:
		out.write("Case #"+str(i+1)+": Bad magician!\n")

