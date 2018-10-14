from collections import deque

def tidy(lst):
	return lst == sorted(lst)

T = int(raw_input())

for qw in range(1, T+1):
	lst = list(raw_input().strip())
	while not tidy(lst):
		for i in range(len(lst) - 1, -1, -1):
			if lst[i] != '9':
				lst[i] = '9'
				for j in range(i - 1, -1, -1):
					if lst[j] != 0:
						lst[j] = str(int(lst[j]) - 1)
						break
					else:
						lst[j] = '9'
				break
	print 'Case #%d:' % qw, int(''.join(lst))
