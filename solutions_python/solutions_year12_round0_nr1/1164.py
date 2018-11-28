import re

def learn():
	Googlerese = ['y qee']
	Googlerese += '''ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv'''.split('\n')
	English = ['a zoo']
	temp = '''Case #1: our language is impossible to understand
Case #2: there are twenty six factorial possibilities
Case #3: so it is okay if you want to just give up'''.split('\n')
	for i in range(len(temp)):
		prefix = re.match(r'^Case #\d+: ', temp[i])
		temp[i] = temp[i][prefix.end():]
	English += temp
	mapping = {' ': ' '}
	for i in range(len(Googlerese)):
		Googlerese[i] = Googlerese[i][-len(English[i]):]
		for j in range(len(Googlerese[i])):
			if ('a' <= Googlerese[i][j] <= 'z' and
				Googlerese[i][j] not in mapping):
				mapping[Googlerese[i][j]] = English[i][j]
	for i in range(ord('a'), ord('z') + 1):
		if chr(i) not in mapping.keys():
			for j in range(ord('a'), ord('z') + 1):
				if chr(j) not in mapping.values():
					mapping[chr(i)] = chr(j)
	return mapping

def solve(input):
	data = input.split('\n')
	T = int(data.pop(0))
	if not 1 <= T <= 30:
		return 'mismatch: 1 <= T <= 30'
	data = data[0:T]
	mapping = learn()
	output = ''
	for X in range(len(data)):
		G = data[X]
		if not len(G) <= 100:
			return 'mismatch: G contains at most 100 characters'
		S = ''
		for j in range(len(G)):
			S += mapping[G[j]] if G[j] in mapping else G[j]
		output += 'Case #%d: ' % (X + 1) + S + '\n'
	return output

import sys
print len(sys.argv)
if len(sys.argv) > 1:
	with open(sys.argv[1]) as f:
		input = f.read()
	output = solve(input)
	print output
	if len(sys.argv) > 2:
		with open(sys.argv[2], 'w') as f:
			f.write(output)