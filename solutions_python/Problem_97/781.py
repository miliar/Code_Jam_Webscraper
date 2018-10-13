def rotate(n):
	n = str(n)
	cycle = []
	length = len(n)

	for i in range(length-1):
		n += n[0]
		n = n[1:]
		cycle.append(int(n))
	return set(cycle)

tc = int(raw_input())
for index in range(tc):
	# Read Input
	a,b = [int(x) for x in raw_input().split()]
	# Initialize
	n = a
	recycled_nums = 0
	used = {}
	for i in range(a,b+1):
		used[i] = 0

	# Compute
	while n <= b:
		cycle = rotate(n)
		for x in cycle:
			if x!=n and x>=a and x<=b and not used[x]:
				recycled_nums += 1
				used[n] = 1
		n += 1
	print 'Case #' + str(index+1) + ': ' + str(recycled_nums)
