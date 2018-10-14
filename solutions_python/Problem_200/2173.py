def tidy_func(x):
	if x < 10:
		return x

	a = []
	x2 = x
	while x > 0:
		a.append(x % 10)
		x //= 10
	a = a[::-1]

	if a.count(0) == len(a)-1:
		return x2-1

	i = len(a) - 1
	while i > 0:
		if a[i] < a[i-1]:
			a[i] = 9
			a[i-1] -= 1
		i -= 1

	if a != sorted(a):
		for i in range(len(a)-1,0,-1):
			if a != sorted(a):
				a[i] = 9
			else:
				break
	x = 0
	for i in range(len(a)):
		x = x*10 + a[i]
	return x


t = int(input().strip())
for i in range(1,t+1):
	print ("Case #{}: {}".format(i,tidy_func(int(input().strip()))))