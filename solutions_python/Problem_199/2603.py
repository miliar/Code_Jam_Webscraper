T = int(raw_input())
for t in range(1,T+1):
	s,k = raw_input().split()
	k = int(k)
	a = []
	for ch in s:
		if ch=='-':
			a.append(1)
		else:
			a.append(0)
	count = 0 
	for i in range(len(a)-k+1):
		if a[i] == 1:
			# print i
			# print a
			count += 1
			for j in range(i,i+k):
				a[j] ^= 1
			# print a
	if sum(a) == 0:
		print 'Case #%d: %d' %(t,count)
	else:
		print 'Case #%d: IMPOSSIBLE' %(t)