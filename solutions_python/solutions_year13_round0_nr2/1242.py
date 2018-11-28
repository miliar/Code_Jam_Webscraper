"""Code written using Python 2.7.2, http://www.python.org/"""

import string

def calc(case):

	for x in range(len(case)):
		maxx = max(case[x])
		for y in range(len(case[x])):
			if case[x][y] < maxx and case[x][y] < max([r[y] for r in case]):
				return 'NO'

	return 'YES'
	

f = open('B-large.in', 'r')
lines = [r.strip() for r in f.readlines()]
f.close()
c = int(lines[0].split()[0])
lines = lines[1:]
#print c

cases = []
while len(lines) > 0:
	rows = int(lines[0].split(' ')[0])
	#print rows
	introws = []
	for row in lines[1:rows+1]:
		introws += [[int(i) for i in row.split(' ')]]

	cases += [introws]
	lines = lines[rows+1:]

#print cases

of = open('output_b_large.txt', 'w')

for idx, case in enumerate(cases):
	of.write('Case #%(idx)i: %(i)s\n' % {'idx': idx + 1, 'i': calc(case)})

of.close()

