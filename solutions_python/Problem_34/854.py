import re

f = open('A-small.in')
L, D, N = [int(i) for i in f.readline()[:-1].split()]
d_words = [f.readline()[:L] for i in range(D)]
n_cases = [f.readline()[:-1] for i in range(N)]
test_str = '+'.join(d_words)
for i, case in enumerate(n_cases):
	p = re.compile(case.replace('(', '[').replace(')', ']+'))
	print 'Case #%d: %d' % (i + 1, len(p.findall(test_str)))
