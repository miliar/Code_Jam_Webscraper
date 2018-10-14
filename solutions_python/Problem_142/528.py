import re

def f(N, words):
	word = words[0]
	pattern = word[0]
	i = 0
	while i < len(word):
		if word[i] != pattern[-1]:
			pattern += word[i]
		i += 1
	regexp = '^' + ''.join([letter + '+' for letter in pattern]) + '$'
	if any(not re.match(regexp, word) for word in words):
		# print pattern
		# print words[0], re.match(regexp, words[0])
		# print words[1], re.match(regexp, words[1])"""
		return 'Fegla Won'
	else:
		pos = [[0] for _ in range(N)]
		for i in range(N):
			for letter in pattern:
				pos[i].append(words[i].index(letter, pos[i][-1]))
			pos[i].append(len(words[i]))
		multiplicity = [[] for _ in range(N)]
		for i in range(N):
			for j in range(1, len(pattern) + 1):
				multiplicity[i].append(pos[i][j + 1] - pos[i][j])
		r = 0
		# r2 = 0
		for j in range(len(pattern)):
			average = int(round(sum(multiplicity[i][j] for i in range(N)) / N))
			r += sum(abs(multiplicity[i][j] - average) for i in range(N))
			# r2 += min(sum(abs(multiplicity[i][j] - k) for i in range(N)) for k in range(max(multiplicity[i][j] for i in range(N)) + 1))
		# if r != r2:
			# print 'CATASTROPHE', r, r2, average
		# if r == 1:
			# print 'Only one'
			# print words[0]
			# print words[1]
		return r

T = int(raw_input())
for i in range(T):
	N = int(raw_input())
	words = []
	for _ in range(N):
		words.append(raw_input())
	r = f(N, words)
	print 'Case #%d: %s' % (i + 1, r)
