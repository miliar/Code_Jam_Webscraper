t = int(input().strip())
for i in range(t):
	d, n = map(int, input().strip().split())
	k = []
	s = []
	for j in range(n):
		x,y = map(int, input().strip().split())
		k.append(x)
		s.append(y)

	slowest = 0
	for j in range(n):
		time = (d-k[j]) / s[j]
		if time > slowest:
			slowest = time

	ans = d / slowest
	print ("Case #{}: {}".format(i+1,ans))