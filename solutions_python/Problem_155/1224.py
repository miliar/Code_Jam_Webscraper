t=int(raw_input())
for i in range(t):
	smax,arr=raw_input().split()
	smax=int(smax)
	arr=map(int,arr)

	frnd=0
	sumsofar=0
	for j in range(len(arr)):
		if(sumsofar>=j):
			sumsofar=sumsofar+arr[j]
		else:
			diff=j-sumsofar
			sumsofar+=diff
			sumsofar+=arr[j]
			frnd+=diff
	print "Case #"+str(i+1)+": "+str(frnd)
110011
