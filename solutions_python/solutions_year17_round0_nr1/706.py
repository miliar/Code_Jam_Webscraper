def flip(t):
	if t=='+':
		return '-'
	return '+'

numruns = int(input())
for run in range(numruns):
	dat = input().split()
	s = dat[0]
	k = int(dat[1])
	count=0
	for i in range(len(s)-k+1):
		if s[i]=='-':
			count+=1
			for j in range(k):
				s=s[0:i+j]+flip(s[i+j])+s[i+j+1:]
	if s=='+'*len(s):
		print('Case #'+str(run+1)+': '+str(count))
	else:
		print('Case #'+str(run+1)+': IMPOSSIBLE')