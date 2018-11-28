def flip(j:int, l:int, pp):
	p=pp
	if int(j) + int(l) > len(p):
		return pp
	for tm in range(j,int(j)+int(l)):
		p[tm] = '+' if p[tm]=='-' else '-'
	return p

for case in range(1,1+int(input())):
	s,k = input().split(' ')
	#print(s,k)
	k = int(k)
	print("Case #%s: " % case,end="")
	i=0
	count = 0
	s = list(s)
	n = len(s)
	if '-' in s:
		t = s.index('-')
		while t<=n-k+1:
			s = flip(t,k,s)
			if '-' in s[:t+1]:
				break
			s = s[t+1:]
			count+=1
			if '-' in s:
				t = s.index('-')
			else:
				break

	if '-' in s:
		print('IMPOSSIBLE')
	else:
		print(count)


