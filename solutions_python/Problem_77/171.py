def solve(size, numbers):	
	ordered =  sorted(numbers)#list(range(1, size + 1))
	total = 0
	for (o,u) in zip(ordered, numbers):
		if o != u:
			total += 1
	return total
'''	
	perms = []
	
	while ordered:
		num = ordered[0]
		perm = set([num])
		perms.append(perm)
		while True:
			res = numbers[num - 1]
			if res in perm:					
				break
			perm.add(res)
			num = res
		for item in perm:
			ordered.remove(item)
	total = 0
#	print "Perms %s" % perms
	for perm in perms:
		l = len(perm)
		if l > 1:
			total += (l - 1)
	return total * 2
'''

N = int(raw_input())
for case in xrange(1, N+1):
	size = int(raw_input())
	numbers = [int(x) for x in raw_input().split()]
	ans = solve(size, numbers)
	print "Case #%d: %f" % (case, ans)
#	print "Numbers %s" % numbers
#	print "        %s" % list(range(1, size + 1))
