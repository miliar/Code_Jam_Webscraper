T = int(input())
for TT in range(T):
	arr = input().split(' ')[1]
	cnt=0
	ans=0
	for i,j in enumerate(arr):
		j=int(j)
		if j and cnt<i:
			ans+=i-cnt
			cnt+=i-cnt
		cnt+=j
	print("Case #%d: %d"%(TT+1,ans))