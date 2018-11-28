# Javier Fernandez Google Code Jam 2013
# Google Code Jam 2013
# javierfdr@gmail.com - javierfdr
# Lawnmower

import sys
import time

# for each cell it has to be possible two traverse
# horizontally or vertically through same or lower level
# lawn
def is_cell_pattern(a,i,j,n,m):
	v = i
	h = m

	#vertically down
	c = v+1
	start = i

	vert_bool = True
	while c<n:
		if not (a[start][j]>= a[c][j]):
			vert_bool = False
		c = c+1


	#vertically up
	c = v-1
	start = i
	while c>=0:
		if not (a[start][j]>= a[c][j]):
			vert_bool = False
		c = c-1


	#horizontally right
	c = h+1
	start = j
	hor_bool = True
	while c<m:
		if not (a[i][start]>= a[i][c]):
			hor_bool = False
		c = c+1

	#horizontally left
	c = h-1
	start = j
	while c>=0:
		if not (a[i][start]>= a[i][c]):
			hor_bool = False
		c = c-1

	if hor_bool==False and vert_bool==False:
		return False

	return True


def is_pattern_possible(a,n,m):
	for i in range(n):
		for j in range(m):
			if not is_cell_pattern(a,i,j,n,m):
				return False
	
	return True


out_file = open('output.out','w+')
in_file = sys.stdin
num_cases = int(in_file.readline())
for c in range(1,num_cases+1):
	case = 'Case #'+str(c)+': '
	r = []

	nm = in_file.readline().strip('\n').split()
	n = int(nm[0])
	m = int(nm[1])

	for i in range(n):
		r.append([int(x) for x in in_file.readline().strip('\n').split()])

	possible = is_pattern_possible(r,n,m)	
	res = ''
	if possible:
		res = 'YES'
	else:
		res = 'NO'


	result = case+res+'\n'
	out_file.write(result)
