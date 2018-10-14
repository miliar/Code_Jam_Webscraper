f = open ("A-large.in", "r")
numbers = f.readline()
L, D, N = map(int, numbers.split(' '))
words = []
patterns = []
for num in range (0, D):
	words.append(f.readline()[:-1])
for num in range (0, N):
	patterns.append(f.readline())
for index, pattern in enumerate(patterns):
	if pattern[-1] == '\n':
		patterns[index] = pattern[:-1]
print patterns

patterndict = {}
for pattern in patterns:
	patterndict[pattern] = []
	tokenlist = pattern.split('(')
	for token in tokenlist:
		if token:
			if token[-1] == ')':
				patterndict[pattern].append(token[:-1])
			elif ')' in token:
				i = token.find(')')
				patterndict[pattern].append(token[:i])
				for char in token[i+1:]:
					patterndict[pattern].append(char)
			else:
				for char in token:
					patterndict[pattern].append(char)	

patterncountdict = {}
for pattern in patterns:
	patterncountdict[pattern] = 0
	tokenlist = patterndict[pattern]
	for word in words:
		valid = True
		for index, letter in enumerate(word):
			if not letter in tokenlist[index]:
				valid = False
		if valid:
			patterncountdict[pattern] += 1

f = open("A-Large.out", "w")
for index, pattern in enumerate(patterns):
	str = "Case #%d: %d" % (index+1, patterncountdict[pattern])
	f.write(str + '\n')
f.close()
			