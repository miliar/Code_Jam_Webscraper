def solve(r,b,y):
	if max(r,b,y)>(r+b+y)/2:
		return 'IMPOSSIBLE'
	solution='RBY'*min(r,b,y)
	solution+='R'*(r-min(r,b,y))
	solution+='B'*(b-min(r,b,y))
	solution+='Y'*(y-min(r,b,y))
	for tmp in range(2):
		for i in range(r+b+y):
			bad=-1
			flip=-1
			for j in range(len(solution)-1):
				if solution[j]==solution[j+1]:
					bad=j
					break
			if bad<0:
				break
			for j in range(len(solution)-1):
				if solution[j]!=solution[bad] and solution[j+1]!=solution[bad]:
					flip=j
					break
			if flip<0:
				solution=solution[0:bad+1]+solution[-1:bad:-1]
			elif flip<bad:
				solution=solution[0:flip+1]+solution[bad:flip:-1]+solution[bad+1:]
			else:
				solution=solution[0:bad+1]+solution[flip:bad:-1]+solution[flip+1:]
		if len(solution)>0:
			solution=solution[1:]+solution[0]
	return solution

numruns=int(input())
for run in range(numruns):
	n,r,o,y,g,b,v = [int(i) for i in input().split()]
	
	print('Case #'+str(run+1)+': ',end='')
	if o>b or g>r or v>y:
		print('IMPOSSIBLE')
		continue
	s = solve(r-g,b-o,y-v)
	if s=='IMPOSSIBLE':
		print(s)
		continue
	if o>0:
		toadd='B'+o*'OB'
		if s=='':
			s=toadd[1:]
		else:
			if 'B' in s:
				s=s.replace('B',toadd,1)
			else:
				print('IMPOSSIBLE')
				continue
	if g>0:
		toadd='R'+g*'GR'
		if s=='':
			s=toadd[1:]
		else:
			if 'R' in s:
				s=s.replace('R',toadd,1)
			else:
				print('IMPOSSIBLE')
				continue
	if v>0:
		toadd='Y'+v*'VY'
		if s=='':
			s=toadd[1:]
		else:
			if 'Y' in s:
				s=s.replace('Y',toadd,1)
			else:
				print('IMPOSSIBLE')
				continue
	print(s)