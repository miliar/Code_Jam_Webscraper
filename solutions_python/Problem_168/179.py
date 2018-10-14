arrow='^>v<'

T=int(raw_input(''))

for cases in range(T):
	ri = map(lambda x: int(x), raw_input('').split(' '))
	R = ri[0]
	C = ri[1]
	
	grid=[]
	target=[]
	acpt=[]
	for i in range(R):
		grid.append(raw_input(''))

	for i in range(R):
		tmp=[] 
		for j in range(C):
			if sum(map(lambda a: a==grid[i][j], arrow)):
				tmp.append(j)
		if len(tmp)==1:
			target.append((i,tmp[0],''))
		elif len(tmp)>=2:
			cnt=0
			last=len(tmp)
			for j in tmp:
				cnt+=1
				target.append((i, j, (cnt==1 or cnt==last) and (cnt==1 and '>' or '<') or '<>'))

	for j in range(C):
		tmp=[]
		for i in range(R):
			if sum(map(lambda a: a==grid[i][j], arrow)):
				tmp.append(i)
		if len(tmp)==1:
			pass
		elif len(tmp)>=2:
			cnt=0
			last=len(tmp)
			for i in tmp:
				cnt+=1
				for ti in range(len(target)):
					if target[ti][0]==i and target[ti][1]==j:
						target[ti] = (target[ti][0], target[ti][1], target[ti][2] + ((cnt==1 or cnt==last) and (cnt==1 and 'v' or '^') or '^v'))
						break

	cnt=0
	for t in target:
		if len(t[2])==0:
			cnt=-1
			break
		elif not sum(map(lambda a: a==grid[t[0]][t[1]], t[2])):
			cnt+=1

	print 'Case #%d: %s' % (cases+1, (cnt==-1 and 'IMPOSSIBLE' or str(cnt)))


