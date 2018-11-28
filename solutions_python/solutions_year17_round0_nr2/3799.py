t = int(raw_input())
q = 1
while t:
	t -= 1
	n = int(raw_input(""))
	arr = [int(d) for d in str(n)]
	lenn = len(arr)
	for i in range(lenn-1,0,-1):
		if arr[i] < arr[i-1]:
			arr[i-1] -= 1
			for j in range(lenn-1,i-1,-1):
				arr[j] = 9
	qq = 0
	for i in arr:
		qq = (qq*10) + i;
	print "Case #%d: %d"%(q,qq)
	q = q + 1