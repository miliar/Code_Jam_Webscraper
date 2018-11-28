from __future__ import print_function
import sys

path = 'A-small-attempt0'

input = open(path + '.in')
output = open(path + '.out', 'w')

B1 = open('A2.in')
B2 = open('A2.out')
B1.readline()
C1 = B1.read()
C2 = ''.join([b[b.find(':') + 2:] for b in B2])
m = {}
m['z'] = 'q'
m['q'] = 'z'
for c, d in zip(C1, C2):
	if c in m and m[c] != d:
		print(c, d)
	m[c] = d
for j in [chr(c + ord('a')) for c in range(26)]:
	if j not in m:
		print('n', j)
	if j not in m.values():
		print('m', j)

T = int(input.readline())
counter = 1
for l in input:
	print('Case #{c}:'.format(c = counter), ''.join(map(lambda a: m[a], l[:-1])), file = output)
	counter += 1
