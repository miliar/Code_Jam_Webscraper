def c(n, k):
	positions_taken = []
	l = [n]
	ls, lr = None, None
	for i in range(k):
		m = max(l)
		for index in range(len(l)):
			if l[index] == m:
				l, ls, lr = put_person_in(l, index)
				break
	return int(max(ls, lr)), int(min(ls, lr))


def put_person_in(l, i):
	n = l[i]

	if n > 2:
		if n % 2 == 0:
			position_taken = n / 2
		else:
			position_taken = (n + 1) / 2 

		ls = position_taken - 1
		lr = n - position_taken

		l.pop(i)
		l.insert(i, lr)
		l.insert(i, ls)
		
		return l, ls, lr
	elif n == 2:
		l[i] = 1
		return l, 0, 1
	# n == 1
	else:
		l.pop(i)
		return l, 0, 0


t = int(raw_input())  # read a line with a single integer


for i in xrange(1, t + 1):
  n, k = [int(x) for x in raw_input().split(" ")]
  minimum, maximun = c(n, k)
  print "Case #{}: {} {}".format(i, minimum, maximun)