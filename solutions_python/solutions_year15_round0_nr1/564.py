t=int(raw_input())
for case in range(t):
	n,s=raw_input().split()
	s=[int(x) for x in s]
	curr=s[0]
	ans=0
	for i in range(1,len(s)):
		if curr<i:
			ans+=1
			curr+=1
		curr+=s[i]

	print "Case #{}: {}".format(case+1,ans)