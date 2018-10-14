def divide(x):
	if x % 2 == 1:
		return x/2, x/2
	else:
		return x/2, x/2-1

def solve(n, k):
	if n == 1: return 0,0
	if k == 1: return divide(n)
	
	queue = list()
	a, b = divide(n)
	if a == b:
		queue.append([a, 2])
	else:
		queue.append([a, 1])
		if b != 0: queue.append([b, 1])

	done = 1

	while True:
		val, count = queue[0]
		if done+count >= k:
			return divide(val)
		else:
			t1, t2 = divide(val)
			if t1 == queue[-1][0]:
				queue[-1][1] += count
			else:
				queue.append([t1, count])

			if t2 == queue[-1][0]:
				queue[-1][1] += count
			else:
				queue.append([t2, count])
			
			done += count
		del queue[0]

	return -1, -1  # not accessible

if __name__ == '__main__':
	t = int(raw_input())  # read a line with a single integer
	for i in xrange(1, t + 1):
	  n, k = [int(s) for s in raw_input().split(" ")]

	  A, a = solve(n, k)
	  print "Case #{}: {} {}".format(i, A, a)