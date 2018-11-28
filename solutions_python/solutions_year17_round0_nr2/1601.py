def lst_to_int(lst):
	tot = 0
	for v in lst:
		tot *= 10
		tot += v
	return tot


def solve(N):
	lst = [int(c) for c in N]
	last_tidy = 0
	while last_tidy + 1 < len(lst) and lst[last_tidy+1] >= lst[last_tidy]:
		last_tidy += 1
	if last_tidy == len(lst) - 1:
		return N
	lst[last_tidy] -= 1
	i = last_tidy - 1
	while i >= 0 and lst[i] == lst[last_tidy]+1:
		lst[i] = lst[last_tidy]
		i -= 1
	start = last_tidy + 1
	if i == -1:
		start = 1
	for i in xrange(start, len(lst)):
		lst[i] = 9
	return lst_to_int(lst)


T = int(raw_input())
for case in xrange(1, T+1):
	N = raw_input()
	print "Case #{}: {}".format(case, solve(N))
