def solve(line):
	numbers = [int(x) for x in line.split(' ')]
	N = numbers[0]
	S = numbers[1]
	p = numbers[2]
	scores = sorted(numbers[3:N+3])
	scores.reverse()
	total = 0
	min_no_surprise = p + max(2 * (p-1), 0)
	i = 0
	while i < N and scores[i] >= min_no_surprise:
		total += 1
		i += 1
	min_with_surprise = p + max(2 * (p-2), 0)
	while i < N and S > 0 and scores[i] >= min_with_surprise:
		total += 1
		i += 1
		S -= 1
	return total
	
		

with open('large.in', 'rb') as fin:
	with open('large.out', 'wb') as fout:
		total_lines = int(fin.readline())
		for i in range(1, total_lines + 1):
			fout.write('Case #%s: %s\n' % (i, solve(fin.readline())))
			fout.flush()