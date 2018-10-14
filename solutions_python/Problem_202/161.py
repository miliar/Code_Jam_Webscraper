# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
import numpy as np

def print_a(ar):
	for row in ar.tolist():
		print("".join(row))
	print("--------------------------------")

def change_a(x, y, c):
	if a[x,y] == '.':
		a[x,y] = c
	else:
		a[x,y] = 'o'
	# print_a(a)
	return 0

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
	n, p = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
	
	count = 0

	a = np.empty((n,n),dtype=np.str)
	a[:,:] = '.'

	mask_row = [0 for i in range(n)]
	mask_col = [0 for i in range(n)]

	mask_dia = [0 for i in range(2*n-1)]
	mask_adia = [0 for i in range(2*n-1)]

	for j in range(p):
		c, x, y = [item for item in str(input()).split()]
		x, y = int(x), int(y)
		a[x-1,y-1] = c
		if c=='x':
			mask_row[x-1] = 1
			mask_col[y-1] = 1
			count += 1
		elif c=='+':
			mask_dia[x-y] = 1
			mask_adia[x+y-2] = 1
			count += 1
		else:
			mask_row[x-1] = 1
			mask_col[y-1] = 1
			mask_dia[x-y] = 1
			mask_adia[x+y-2] = 1
			count += 2
	
	ori_a = a.copy()


	# print("Case {}--------------------------------------------".format(i))
	# print_a(a)

	for x in range(n):
		# print_a(a)
		for y in range(n):
			if not mask_row[x] and not mask_col[y]:
				mask_row[x] = 1
				mask_col[y] = 1
				count += 1
				change_a(x, y, 'x')
				break
	

	x = 0
	for y in range(n):
		v = x-y
		w = x+y
		if not mask_dia[v] and not mask_adia[w]:
			mask_dia[v] = 1
			mask_adia[w] = 1
			count += 1
			change_a(x, y, '+')
	x = n-1
	for y in range(1, n-1):
		v = x-y
		w = x+y
		if not mask_dia[v] and not mask_adia[w]:
			mask_dia[v] = 1
			mask_adia[w] = 1
			count += 1
			change_a(x, y, '+')

	r = []

	for x in range(n):
		for y in range(n):
			if a[x,y] != ori_a[x,y]:
				r.append((a[x,y], x+1, y+1))


	print("Case #{}: {} {}".format(i, count, len(r)))

	# print_a(a)

	for c, x, y in r:
		print("{} {} {}".format(c, x, y))


	# check out .format's specification for more formatting options
