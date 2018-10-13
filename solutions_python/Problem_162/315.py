def removeTrailing(n):
	if n%10==0:
		return n-1
	return n
def revers1(n):
	n=str(n)
	n=n[::-1]
	return int(n)
arr=[-1]*(10**6+1)
arr[1]=1
for i in range(1,10**6):
	if arr[i+1]==-1:
		arr[i+1]=arr[i]+1
	else:
		arr[i+1]=min(arr[i+1],arr[i]+1)
	rev=revers1(removeTrailing(i))
	if rev <= 10**6:
		if arr[rev]==-1:
			arr[rev]=arr[i]+1

t=int(raw_input())
for case in range(t):
	n=int(raw_input())	
	print "Case #{}: {}".format(case+1,arr[n])


