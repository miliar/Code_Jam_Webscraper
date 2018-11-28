T = int(raw_input())

for h in range(T):
	c = map(lambda x: int(x), raw_input().split(" "))
	L = c.pop(0)
	t = c.pop(0)
	N = c.pop(0)
	C = c.pop(0)
	
	arr = []
	for i in range(N):
		arr.append(c[i%C] * 2)

	s = []
	for k in range(0,L):
		total = 0
		for i in range(N):
			total += arr[i]
			if total >= t:
				max = -1
				l = -1
				if i not in s:
					l = i
					max = (total - t)/2

				for j in range(i+1,N):
					if j not in s and max < arr[j]/2:
						l = j
						max = arr[j]/2

				if max != -1:
					s.append(l)
					arr[l]-=max
					break

	print "Case #%d: %d" % (h+1, sum(arr))
	