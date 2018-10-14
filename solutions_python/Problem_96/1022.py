def possible_scores(total):
	"""(unsurprising, surprising)"""
	base = total / 3
	if total == 0:
		return (0, 0)
	if total > 28:
		return (10, 10)
	if total % 3 == 0:
		return (base, base+1)
		# 1 1 1; 0 1 2
	elif total % 3 == 1:
		return (base+1, base+1)
		# 1 1 2; 0 2 2
	elif total % 3 == 2:
		return (base+1, base+2)
		# 1 2 2; 1 2 3

def solve_one(line):
	words = map(int, line.split(" "))
	n, s, p = words[:3]
	scores = map(possible_scores, words[3:])
	assert len(scores) == n
	achieved_p = len([x for x, y in scores if x >= p])
	need_surprise = len([x for x, y in scores if x < p and y >= p])
	return achieved_p + min(need_surprise, s)

def solve(inp):
	output = []
	for line, i in zip(inp.split("\n")[1:], range(1, 1000)):
		output.append("Case #%d: %s" % (i, solve_one(line)),)
	result = "\n".join(output)
	open("B.out", "w").write(result)
	return result
