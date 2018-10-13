def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, a % b)

fp = open('b.in')
t = int(fp.readline())

for i in range(0, t, 1):
	data = fp.readline()
	arr = data.split()	
	n = int(arr[0])
	g = -1
	for j in range(0, n, 1):
		for k in range(j + 1, n, 1):
			value = abs(int(arr[j+1]) - int(arr[k+1]))
			if g == -1:
				g = value
			else:
				g = gcd(g, value)
			
	ret = int(arr[1]) % g
	if ret != 0:
		ret = g - ret

	print "Case #" + str(i + 1) + ": " + str(ret)	
