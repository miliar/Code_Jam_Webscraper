from collections import deque

T = int(raw_input())

def Append(lst, val):
	if len(lst) > 0 and lst[-1][0] == val[0]:
		lst[-1] = (val[0], lst[-1][1] + val[1])
	else:
		lst.append(val)

for qw in range(1, T+1):
	n, k = map(int, raw_input().strip().split())
	lst = deque()
	lst.append((n, 1))
	while True:
		num, cnt = lst.popleft()
		if cnt >= k:
			break
		k = k - cnt
		Append(lst, ((num - 1) - (num - 1) // 2, cnt))
		Append(lst, ((num - 1) // 2, cnt))
		# print lst
	print 'Case #%d: %d %d' % (qw, (num - 1) - (num - 1) // 2, (num - 1) // 2)
