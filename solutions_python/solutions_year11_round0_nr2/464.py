def int_input():
	return int(raw_input())

def case_input():
	result = [[], [], []]
	i = -1
	
	for token in raw_input().split():
		try:
			int(token)
			i += 1
		except ValueError:
			result[i].append(token)
	
	result.append(result.pop(-1).pop(-1))
	return result

def combine(cbs, li):
	last2 = li[-2:]
	if len(last2) >= 2:
		for cb in cbs:
			if (last2[0] == cb[0] and last2[1] == cb[1]) or (last2[0] == cb[1] and last2[1] == cb[0]):
				li.pop(-1)
				li.pop(-1)
				li.append(cb[2])
				return True
	return False

def oppose(ops, li):
	last2 = li[-2:]
	if len(last2) >= 2:
		for op in ops:
			if op[0] in li and op[1] in li:
				del li[:]
				return True
	return False	

def solve(c):
	cbs, ops, sq = case_input()
	li = []
	marks = {}
	for ch in sq:
		li.append(ch)
		if not combine(cbs, li):
			oppose(ops, li)
	print 'Case #%d: %s' % (c, str(li).replace("'", ""))

def main():
	for c in range(int_input()):
		solve(c+1)

main()
