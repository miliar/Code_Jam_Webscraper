t=input()
for a in range(t):
	[n,k]=map(int,raw_input().split())
	filled=[0,n+1]
	filled_len=2
	for j in range(k):
		maxi=filled[1]-filled[0]
		left=0
		right=1
		for l in range(2,filled_len):
			if(filled[l]-filled[l-1]>maxi):
				maxi=filled[l]-filled[l-1]
				left=l-1
				right=l
		filled.insert(right,(filled[left]+filled[right])/2)
		filled_len+=1
		if(j==k-1):
			ls=filled[right]-filled[right-1]-1
			rs=filled[right+1]-filled[right]-1
			if(ls>rs):
				print "Case #"+str(a+1)+": "+str(ls)+" "+str(rs)
			else:
				print "Case #"+str(a+1)+": "+str(rs)+" "+str(ls)
