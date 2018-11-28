for t in xrange(int(raw_input())):
	s,k = map(str,raw_input().split())
	k,n = int(k),len(s)
	s = list(s)
	i,flag,ans = 0,True,0
	while i<n:
		if s[i]=='-':
			if n-i<k:
				flag = False
				break
			else:
				ans += 1
				for j in xrange(i,i+k):
					s[j] = '+' if s[j]=='-' else '-'
		i+=1
		#print ''.join(s)
	if flag:
		print "Case #"+str(t+1)+":",ans
	else:
		print "Case #"+str(t+1)+":","IMPOSSIBLE"
