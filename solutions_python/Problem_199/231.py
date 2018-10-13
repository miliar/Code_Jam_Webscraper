def h(sign):
	return sign == '+'

def reverse(sign):
	if sign == '+':
		return '-'
	else:
		return '+'

def flip(lst):
	lst.reverse()
	return list(map(reverse, lst))

def best(inputs, k):
	count = 0
	for i in range(len(inputs) - k + 1):
		if not h(inputs[i]):
			count += 1
			for j in range(i, i + k):
				inputs[j] = reverse(inputs[j])
	for i in range(len(inputs) - k + 1, len(inputs)):
		if not h(inputs[i]):
			return "IMPOSSIBLE"
	return count

def solve(case_number):
	panks, k = [s for s in raw_input().split(" ")]
	ans = best(list(panks), int(k))
	print "Case #{}: {}".format(case_number, ans)

t = int(raw_input())  # read a line with a single integer
for case in xrange(1, t + 1):
	solve(case)

'''
python solution.py <small.in> small.out
python solution.py <large.in> large.out
'''