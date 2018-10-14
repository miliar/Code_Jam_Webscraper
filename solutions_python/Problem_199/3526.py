x=int(input())
for i in range(1,x+1):
	s=raw_input()
	a1,a2=s.split()
	a2=int(a2)
	a1=list(a1)
	cnt=0
	le=len(a1)
	flag=True
	for j in range(0,le):
		if a1[j]=='+':
			continue
		elif a1[j]=='-' and j+a2<=le:
			cnt+=1
			for k in range(j,j+a2):
				a1[k]= '-' if a1[k]=='+' else '+'
		else:
			flag=False
			break
	if not flag:
		cnt='IMPOSSIBLE'
	print 'Case #%s: %s' % (str(i), str(cnt))

