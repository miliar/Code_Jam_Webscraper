f = open("tidy.input", "r")
T = int(f.readline())

k = 0
for line in f:
	num_str = str(int(line))
	l = []
	n = len(num_str)
	for c in num_str:
		l.append(c)
	# print(n, l)

	q = -1
	p = 1
	r = 0
	for i in range(n-1):
		if(int(l[i]) > p):
			p = int(l[i])
			r = i
		if(int(l[i]) > int(l[i+1])):
			q=i
			break
	# print(q, p,r)
	ans = int(''.join(l))

	if(q == -1):
		print("Case #{}: {}".format(k+1, int(ans)))
	else:
		# make tidy
		tidier = l[r+1:]
		todo = int(''.join(tidier)) + 1
		# print(tidier, todo)
		ans = ans - todo
		print("Case #{}: {}".format(k+1, int(ans)))
	k += 1