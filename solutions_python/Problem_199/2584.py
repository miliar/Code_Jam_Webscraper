t = int(raw_input())
for n in xrange(1,t+1):
	cnt=0
	s,k = [s for s in raw_input().split(" ")]
	k=int(k)
	l = len(s)
	if s.count('-') !=0 :
		for i in range(l):
			if s[i]=='-' and i+k-1<l:
				for j in range(k):
					if s[i+j]=='-':
						s=s[0:i+j]+'+'+s[i+j+1:l]
					else:
						s=s[0:i+j]+'-'+s[i+j+1:l]
				cnt+=1
								
	if '-' in s:
		print "Case #{}: IMPOSSIBLE".format(n)

	else:				
		print "Case #{}: {}".format(n,cnt)
