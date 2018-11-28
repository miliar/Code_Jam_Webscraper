def is_solved(line):
	return all(s == True for s in line)

def flip(line, start, size):
	if start + size > len(line):
		raise IndexError
	for i in range(size):
		line[start+i] = not line[start+i]
	return line

ln = int(input())
for case in range(ln):
	parsed = input().split(' ')
	line = parsed[0]
	size = int(parsed[1])
	line = list(map(lambda s: True if s == '+' else False, line))
	num_flips = 0
	for i, c in enumerate(line):
		if is_solved(line):
			break
		if c == False:
			try:
				flip(line, i, size)
				num_flips += 1
				if is_solved(line):
					break
			except IndexError:
				break
	if is_solved(line):
		print('Case #%d: %d' % (case + 1, num_flips))
	else:
		print('Case #%d: IMPOSSIBLE' % (case + 1))


