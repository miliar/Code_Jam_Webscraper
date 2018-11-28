from math import *

def to_set(r, value):
	res = set()
	i = ceil(value / r) * r
	while value / i >= 0.9:
		res.add(i // r)
		i += r

	i = floor(value / r) * r
	while i > 0 and value / i <= 1.1:
		res.add(i // r)
		i -= r

	return res

def solve(lists, raw_lists):
	res = 0
	while not [] in lists:
		first_column = [row[0] for row in lists]
		first_column_raw = [row[0] for row in raw_lists]
		u = set.intersection(*first_column)
		if u:
			# print(first_column_raw)
			for l in lists:
				l.pop(0)
			for l in raw_lists:
				l.pop(0)
			res += 1
		else:
			index = first_column.index(min(first_column))
			lists[index].pop(0)
			raw_lists[index].pop(0)
	return res

T = int(input())

for t in range(1, T + 1):
	n, p = [int(x) for x in input().split()]
	R = [int(x) for x in input().split()]

	lists = []
	raw_lists = []
	for i in range(n):
		raw = sorted([int(x) for x in input().split()])
		sets = []
		for x in raw:
			sets.append(to_set(R[i], x))
		raw_lists.append(raw)
		lists.append(sets)
	# print(lists)
		# print(R[i], ":", raw)
	print('Case #%d: %d' % (t, solve(lists, raw_lists)))
