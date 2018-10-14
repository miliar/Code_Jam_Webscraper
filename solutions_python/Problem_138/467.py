from collections import deque

t = int(raw_input())

for i in xrange(t):
	n = int(raw_input())
	naomi = [float(x) for x in raw_input().split()]
	ken = [float(x) for x in raw_input().split()]
	n1 = deque(sorted(naomi))
	k1 = deque(sorted(ken))
	n2 = deque(sorted(naomi))
	k2 = deque(sorted(ken))
	ans_w = 0
	ans_dw = 0
	for j in xrange(n):
		if n1[0] < k1[0]:
			n1.popleft()
			k1.popleft()
		else:
			n1.pop()
			k1.popleft()
			ans_w += 1
	for k in xrange(n):
		if n2[0] < k2[0]:
			k2.pop()
			n2.popleft()
		else:
			n2.popleft()
			k2.popleft()
			ans_dw += 1
	print 'Case #%d: ' %(i+1) + str(ans_dw) + ' ' + str(ans_w)