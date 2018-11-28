d = {}
def g(a, i, j):
	# print(a[i][j], a[i-1][j], d.get(a[i-1][j], 2))
	if j > 0 and a[i][j-1] != '?' and d.get(a[i][j-1], 1) == 1:
		a[i][j] = a[i][j-1]
		d[a[i][j]] = 1
		# print('1:', a[i][j], d[a[i][j]])
	elif j < m-1 and a[i][j+1] != '?' and d.get(a[i][j+1], 1) == 1:
		a[i][j] = a[i][j+1]
		d[a[i][j]] = 1
		# print('1:', a[i][j], d[a[i][j]])
		# print(a[i][j])
	elif i > 0 and a[i-1][j] != '?' and d.get(a[i-1][j], 2) == 2:
		# print(a[i][j], d[a[i][j]])
		a[i][j] = a[i-1][j]
		d[a[i][j]] = 2
	elif i < n-1 and a[i+1][j] != '?' and d.get(a[i+1][j], 2) == 2:
		a[i][j] = a[i+1][j]
		d[a[i][j]] = 2

def to_str(a):
	return '\n'.join(''.join(i) for i in a)

def myindex(l):
	if '?' not in l:
		return -1
	for i in range(m):
		if l[i] != '?':
			if i != 0:
				return i-1
			else:
				return l.index('?')
	return -1

def f(a):
	global d
	d.clear()
	flag = True
	# for k in range(3):
	while '?' in to_str(a):
		flag = False
		for i in range(n):
			# for j in range(m):
			j = myindex(a[i])
			# print('j', j)
			if j >= 0 and a[i][j] == '?':
				flag = True
				g(a, i, j)
		# print('\n'.join(''.join(i) for i in a))
	return a

t = int(input())
for it in range(1, t+1):
	n, m = map(int, input().split())
	a = []
	for i in range(n):
		inp = input()
		if inp.count('?') == m:
			if i != 0:
				a.append(a[-1])
			else:
				a.append([])
		else:
			a.append(list(inp))
	for i in range(n-2, -1, -1):
		if a[i] == []:
			a[i] = a[i+1]
	print("Case #%d:" % it)
	f(a)
	print(to_str(a))
