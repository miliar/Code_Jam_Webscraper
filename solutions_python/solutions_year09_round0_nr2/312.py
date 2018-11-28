#Watersheds. GCJ Qualis
values=[[0,0],[-1,0],[0,-1],[0,1],[1,0]]
ops=[-1,4,3,2,1]
alph=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
t=int(raw_input())
for s in xrange(t):
	print "Case #"+str(s+1)+":"
	heights=[]
	directions=[]
	sinks=[]
	belongs=[]
	groups=[True]*26
	h,w=map(int,raw_input().split())
	heights+=[[10000]*(w+2)]
	for i in xrange(h):
		heights+=[map(int,raw_input().split())]
		heights[i+1][0:0]=[10000]
		heights[i+1].append(10000)
	heights+=[[10000]*(w+2)]

	#for i in heights[1:-1]:
	#	print i[1:-1]
		
	directions+=[[0]*(w*2)]
	for i in xrange(h):
		directions.append([0]*(w+2))
		belongs.append([0]*w)
		for j in xrange (w):
			small=0
			for k in xrange(1,5):
				#print (i+1),";",(j+1),"->",heights[i+1+values[small][0]][j+1+values[small][1]]
				#print (i+1),";",(j+1),"?>",i+1+values[k][0],";",j+1+values[k][1]
				#print (i+1),";",(j+1),"?>",heights[i+1+values[k][0]][j+1+values[k][1]]
				if heights[i+1+values[small][0]][j+1+values[small][1]]>heights[i+1+values[k][0]][j+1+values[k][1]]:
					small=k
			directions[i+1][j+1]=small
			if small==0:
				sinks+=[[[i,j]]]
	directions+=[[0]*(w+2)]
	#print "0-sink | 1-Up | 2-Left | 3-Right | 4-Down"
	#for i in directions[1:-1]:
	#	print i[1:-1]
		
	for i in xrange(len(sinks)):
		q=[sinks[i][0]]
		while len(q)>0:
			cur=q.pop()
			belongs[cur[0]][cur[1]]=i
			for j in xrange(1,5):
				if directions[1+cur[0]+values[j][0]][1+cur[1]+values[j][1]]==ops[j]:
					q.append([cur[0]+values[j][0],cur[1]+values[j][1]])
	count=0
	#for i in belongs:
	#	print i
	#print
	for i in belongs:
		for j in i:
			if groups[j]==True:
				groups[j]=alph[count]
				count+=1
			print groups[j],
		print