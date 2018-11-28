t = int(input())
for index in range(t):
	n,k = input().split()
	n = int(n)
	k = int(k)
	d = {}
	d[n] = 1
	people = 0
	while people <= k-1:
		key = max(d.keys())
		v = d[key]
		d.pop(key, None)
		if key%2==1:
			j = (key-1)//2
			if j not in d:d[j] = 0
			d[j] += 2*v
			a=b=j
		else:
			j = key//2
			if j not in d:d[j] = 0
			if j-1 not in d:d[j-1] = 0
			d[j] += v
			d[j-1] += v
			a = j
			b = j-1
		people += v
	print("Case #"+str(index+1)+": "+str(a)+" "+str(b))
