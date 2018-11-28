
def flip(pattern, k):
	limit = 0
	while True:
		if pattern >> limit != 0:
			limit = limit + 1
		else:
			break

	num = 0
	flipper = 2**k-1
	while pattern != 0:
		if (pattern & 1) == 1:
			pattern = (pattern ^ flipper) >> 1
			num = num + 1
		else:
			pattern = pattern >> 1

		if num > limit:
			return -1

	return num



with open('A-large.in') as f_in:
	T = int(f_in.readline())
	nums = []
	for i in xrange(T):
		pattern, k = f_in.readline().split(' ')
		pattern = pattern.replace('+', '0').replace('-', '1')
		pattern = int(pattern, 2)

		num = flip(pattern, int(k))
		nums.append(num)

with open('A-large.out', 'w') as f_out:
	for i in xrange(T):
		f_out.write('Case #' + str(i+1) + ': ')
		if nums[i] == -1:
			f_out.write('IMPOSSIBLE\n')
		else:
			f_out.write(str(nums[i]) + '\n')
