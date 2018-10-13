from __future__ import print_function
import os, os.path
directory = 'C:\Users\lucho\Desktop\___tests'
files = os.listdir(directory)

fp = open(os.path.join(directory, files[0]), 'rb')
fp2 = open(os.path.join(directory, '..', 'out1.txt'), 'wb')

lines = iter(map(lambda x: x.strip(), fp.readlines()))

# functions go here

tests = int(next(lines))
for i in range(tests):
	r, c = map(int, next(lines).split())
	m = []
	for j in range(r):
		m.append(list(next(lines)+' '))
	m.append([' '] * c)

	possible = True
	for y in range(len(m)):
		for x in range(len(m[y])):
			if m[y][x] == '#':
				if m[y][x+1] == '#' and m[y+1][x] == '#' and m[y+1][x+1] == '#':
					m[y][x] = '/'
					m[y][x+1] = '\\'
					
					m[y+1][x] = '\\'
					m[y+1][x+1] = '/'
					continue
				else:
					possible = False
					break
		
		if not possible: break
			

	print('Case #%d:' % (i+1), file=fp2)
	if not possible:
		print('Impossible', file=fp2)
	else:
		for row in m[:-1]:
			print((''.join(row)).strip(), file=fp2)

fp.close()
fp2.close()
