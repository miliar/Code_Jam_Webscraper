import sys

sys.stdin = open("A-large.in", 'r')
sys.stdout = open("out.out", 'w')

T = input()
for t in xrange(T):
	lst, k = raw_input().split()
	k = int(k)
	orig = map(lambda x: 1 if x == "+" else 0, list(lst))
	lst = orig + [1]
	left = lst[0:k]
	lmov = 0
	for i in xrange(k, len(lst)):
		if left[0] == 0:
			for j in xrange(k):
				left[j] += 1
				left[j] %= 2
			lmov += 1
		
		left.pop(0)
		left.append(lst[i])
	flag = False
	if left == [1 for i in xrange(k)]:
		flag = True
	lst = orig[::-1] + [1]
	right = lst[0:k]
	rmov = 0
	for i in xrange(k, len(lst)):
		if right[0]%2 == 0:
			for j in xrange(k):
				right[j] += 1
			rmov += 1
		right.pop(0)
		right.append(lst[i])

	if right == [1 for i in xrange(k)]:
		flag = True
	print "Case #%d: %s"%(t+1, str(min(lmov, rmov)) if flag else "IMPOSSIBLE")