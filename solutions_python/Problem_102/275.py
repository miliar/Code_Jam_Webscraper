t = int(raw_input().strip())
t_count = 1
while t_count <= t:
	line = [int(x) for x in raw_input().strip().split()]
	total = sum(line[1:])
	n = line[0]
	min_score = float(total * 2) / float(n)
	answers = list()
	weighted_total = total
	for i in line[1:]:
		if i > min_score:
			n -= 1
			answers.append(float(0))
		else:
			weighted_total += i
			answers.append(-1)
	answer = 'Case #%d:' % (t_count,)
	min_score = float(weighted_total) / float(n)
	pointer = 0
	while pointer < line[0]:
		if answers[pointer] == -1:
			ans = float(min_score - line[pointer + 1]) / float(total)
		else:
			ans = 0
		ans *= 100
		answers[pointer] = ans
		answer = '%s %f' % (answer, ans,)
		pointer += 1
	print answer
	t_count += 1
