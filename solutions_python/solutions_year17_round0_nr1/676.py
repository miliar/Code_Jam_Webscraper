import queue

# def solve(l, k):
# 	visited = set()
# 	level = queue.Queue()
# 	prevLevel = queue.Queue()
# 	prevLevel.put(l)
# 	rounds = 0
# 	useful = 1
# 	while useful:
# 		useful = 0
# 		while not prevLevel.empty():
# 			s = prevLevel.get()
# 			if not s in visited:
# 				visited.add(s)
# 				useful = 1
# 				# print(s)
# 				if verify(s):
# 					return rounds
# 				for i in range(len(s)-k+1):
# 					t = flip(s, i, k)
# 					# print('\t', t)
# 					level.put(t)
# 		prevLevel = level
# 		level = queue.Queue()
# 		# print(rounds)
# 		rounds+=1
# 	return None

# def verify(s):
# 	for c in s:
# 		if c == '-': return False
# 	return True

def neg(c):
	if c == '+': return '-'
	return '+'

def flip(l, j, k):
	for i in range(k):
		l[j+i] = neg(l[j+i])

def solve(s, k):
	l = list(s)
	count = 0
	for i in range(len(l)-k+1):
		if l[i] == '-':
			flip(l, i, k)
			count += 1
	for c in l[-k:]:
		if c == '-': return None
	return count

print(solve("---+-++-", 3))

if __name__ == '__main__':
	fname = 'A-large.in'
	oname = 'p1.out'
	f = open(fname, 'r')
	g = open(oname, 'w+')
	first = True
	case = 1
	for line in f:
		ans = "IMPOSSIBLE"
		if first: first = False
		else:
			strs = line.split(' ')
			a = solve(strs[0], int(strs[1]))
			if a is not None: ans = a
			g.write("Case #{0}: {1}\n".format(str(case), str(ans)))
			case+=1