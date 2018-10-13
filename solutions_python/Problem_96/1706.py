with open('B-large.in', 'r') as fin, open('B-large.out', 'w') as fout:
	fin.readline()
	for i, line in enumerate(fin):
		nums = list(map(int, line.split(' ')))
		(dummy, surprising, best) = nums[0:3]
		scores = nums[3:]
		unsurprising_high = len([x for x in scores if max(3*best - 2, best) <= x])
		possible_surprising_high = len([x for x in scores if max(3*best - 4, best) <= x])
		max_high = min(possible_surprising_high, unsurprising_high + surprising)
		fout.write('Case #' + str(i+1) + ': ' + str(max_high) + '\n')
