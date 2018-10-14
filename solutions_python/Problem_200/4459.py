def get_number(n):
	lis = []
	l = str(n)
	for i in l:
		lis.append(int(i))

	return (all(lis[i] <= lis[i+1] for i in xrange(len(lis)-1)))


case = 0

case = input()

for x in range(1, case+1):
	last = 1
	n = 0
	n = input()
	t = False

	for i in xrange(n, 0, -1):
		if i % 10 != 0:
			t = get_number(i)
			if t:
				last = i
				break

	print ('Case #{}: {}'.format(x, i))

			
