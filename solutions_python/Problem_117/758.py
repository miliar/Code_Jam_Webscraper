from copy import deepcopy

f=open("./large.txt")
#t number of patterns

def canDo(l,nrow,ncol):
	max_height=max([max(row) for row in l])
	if max_height>100:
		return 'NO'
	else:
		#generate max-l
		l_init=deepcopy(l)
		for i in range(nrow):
			for j in range(ncol):
				l_init[i][j]=max_height
	Search=True
	while l_init!=l and Search:
		Search=False
		for i in range(nrow):
			current=l_init[i]
			target=l[i]
			h=max(target)
			if any([current[item]>h for item in range(ncol)]):
				Search=True
				for j in range(ncol):
					if l_init[i][j]>=h:
						l_init[i][j]=h
				#print i,h, l_init

		for i in range(ncol):
			current=[l_init[j][i] for j in range(nrow)]
			target=[l[j][i] for j in range(nrow)]
			h=max(target)
			if any([current[item]>h for item in range(nrow)]):
				Search=True
				for j in range(nrow):
					if l_init[j][i]>=h:
						l_init[j][i]=h

	if l_init==l:
		return 'YES'
	else:
		return 'NO'



t=int(f.readline()[:-1])

with open('./out.txt','w') as fout:
	for i in range(1,t+1):
		line=f.readline()[:-1].split(" ")
		N=int(line[0])
		M=int(line[1])
		lawn=[]
		for j in range(N):
			if i==t and j==N-1:
				line=f.readline().split(" ")
			else:
				line=f.readline()[:-1].split(" ")
			lawn.append([int(item) for item in line])
		str='Case #%i: %s\n' %(i,canDo(lawn,N,M))
		fout.write(str)
