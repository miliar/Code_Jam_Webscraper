t = int(raw_input())
for ti in xrange(t):
	n = int(raw_input())
	temp = n
	arr = []
	while(temp>0):
		arr.append(temp%10)
		temp = temp/10
	
	for i in xrange(len(arr)-1):
		if (arr[i]<arr[i+1]):
			for j in xrange(i+1):
				arr[j] = 9
			arr[i+1] = arr[i+1] - 1

	arr.reverse()
	val = 0
	for i in arr:
		val = 10*val + i
	print "Case #"+str(ti+1)+": "+str(val)