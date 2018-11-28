
import re

L, D, N = map(int, raw_input().split())

words = [raw_input().strip() for i in range(D)]
assert all(len(w) == L for w in words)

cases = [raw_input().strip() for i in range(N)]

def VarToBits(v):
	return reduce(lambda x, y: x|y, [1 << (ord(c) - ord('a')) for c in v])


def MakeSets(str):
	regexp = '^' + L*r'(([a-z])|\(([a-z]+)\))' + '$'
	m = re.match(regexp, str)
	assert m, '[%s]' % str
	vars = [m.group(1+ 3*i+1) or m.group(1+ 3*i+2) for i in range(0, L)]
	sets = [VarToBits(v) for v in vars]
	return sets

	
case_sets = [MakeSets(c) for c in cases]
words_sets = [ [VarToBits(c) for c in word] for word in words ]

#print words
#print cases

for i, case_set in enumerate(case_sets):
	case_i = i + 1
	fit_num = sum(all(c&char_set for c, char_set in zip(word, case_set)) for word in words_sets)
	print 'Case #%d: %d' % (case_i, fit_num)
	