def play(N, R, P, S):
	total = R + P + S
	half = total / 2
	if R > half or P > half or S > half:
		return 'IMPOSSIBLE'
	if total == 2:
		res = ''
		if P:
			res += 'P'
		if R:
			res += 'R'
		if S:
			res += 'S'
		return res
	AR = (R + S - P) / 2
	AS = (P + S - R) / 2
	AP = (R + P - S) / 2
	next = play(N, AR, AP, AS)
	if next == 'IMPOSSIBLE':
		return 'IMPOSSIBLE'
	else:
		if N == total:
			res = []
			for i in next:
				if i == 'R':
					res += ['RS']
				elif i == 'P':
					res += ['PR']
				else:
					res += ['PS']
			return res
		else : 
			res = ''
			for i in next:
				if i == 'R':
					res += 'RS'
				elif i == 'P':
					res += 'PR'
				else:
					res += 'PS'
			return res

def sor(strs, N, total):
	for i in range(N - 1):
		new_strs = []
		length = 2 ** (N - i - 2)
		for e in range(length):
			a = strs[2 * e]
			b = strs[2 * e + 1]
			if b < a:
				a, b = b, a
			new_strs += [a + b]
		strs = new_strs
	return ''.join(strs)


def solve(case_number):
	input_numbers = [int(s) for s in raw_input().split(" ")]
	N, R, P, S = input_numbers
	total = 2 ** N
	ans = play(total, R, P, S)
	if ans == 'IMPOSSIBLE':
		print "Case #{}: {}".format(case_number, ans)
		return
	if N > 1:
		ans = sor(ans, N, total)
	print "Case #{}: {}".format(case_number, ans)

t = int(raw_input())  # read a line with a single integer
for case in xrange(1, t + 1):
	solve(case)



'''
python solution.py <small.in> small.out
python solution.py <large.in> large.out
'''