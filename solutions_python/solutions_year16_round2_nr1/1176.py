def solve(s, l):
	if 'Z' in s:
		l.append(0)
		for letter in 'ZERO':
			s = s.replace(letter, '', 1)
		return solve(s, l)
	if 'W' in s:
		l.append(2)
		for letter in 'TWO':
			s = s.replace(letter, '', 1)
		return solve(s, l)
	if 'U' in s:
		l.append(4)
		for letter in 'FOUR':
			s = s.replace(letter, '', 1)
		return solve(s, l)
	if 'X' in s:
		l.append(6)
		for letter in 'SIX':
			s = s.replace(letter, '', 1)
		return solve(s, l)
	if 'G' in s:
		l.append(8)
		for letter in 'EIGHT':
			s = s.replace(letter, '', 1)
		return solve(s, l)
	if ('S' in s) and ('E' in s) and ('V' in s) and ('E' in s) and ('N' in s):
		l.append(7)
		for letter in 'SEVEN':
			s = s.replace(letter, '', 1)
		return solve(s, l)
	if ('T' in s) and ('H' in s) and ('R' in s) and ('E' in s) and ('E' in s):
		l.append(3)
		for letter in 'THREE':
			s = s.replace(letter, '', 1)
		return solve(s, l)
	if ('F' in s) and ('I' in s) and ('V' in s) and ('E' in s):
		l.append(5)
		for letter in 'FIVE':
			s = s.replace(letter, '', 1)
		return solve(s, l)
	if ('N' in s) and ('I' in s) and ('N' in s) and ('E' in s):
		l.append(9)
		for letter in 'NINE':
			s = s.replace(letter, '', 1)
		return solve(s, l)
	if ('O' in s) and ('N' in s) and ('E' in s):
		l.append(1)
		for letter in 'ONE':
			s = s.replace(letter, '', 1)
		return solve(s, l)
	if s == '':
		l.sort()
		return "".join(map(str,l))


lines = open('A-large.in', 'r').readlines()[1:]
for i, line in enumerate(lines):
	print 'Case #%i: %s' % (i+1, solve(line.strip(), []))



