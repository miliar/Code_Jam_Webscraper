inp = open("C-small-attempt4.in", "r")
R=lambda:map(int, inp.readline().strip().split(' '))
SR=lambda:map(str, inp.readline().strip().split(' '))
outp = open("output.txt", "w")

tab = {"1" : {"1" : "1", "i" : "i", "j" : "j", "k" : "k"},
	   "i" : {"1" : "i", "i" : "-1", "j" : "k", "k" : "-j"},
	   "j" : {"1" : "j", "i" : "-k", "j" : "-1", "k" : "i"},
	   "k" : {"1" : "k", "i" : "j", "j" : "-i", "k" : "-1"}}

def swap_neg(a, b):
	if b[0] == '-':
		return '-' + a, b[1]
	return a, b

def mulit(a, b):
	neg = False
	if a[0] == '-':
		a = a[1]
		neg = True
	if b[0] == '-':
		b = b[1]
		if neg:
			neg = False
		else:
			neg = True
	c = tab[a][b]
	if neg:
		if c[0] == '-':
			return c[1]
		else:
			return '-' + c
	return c

def mulit_all(arr):
	cur = '1'
	for i in arr:
		cur = mulit(cur, i)
	return cur

def find_all_i(arr):
	cur = '1'
	ret = []
	oldi = -1
	for i in xrange(len(arr)):
		cur = mulit(cur, arr[i])
		if cur == 'i' and oldi == -1:
			oldi = i
	return [cur], oldi

def find_all_k(arr):
	cur = '1'
	ret = []
	lastk = -1
	for i in xrange(len(arr)):
		c = arr[len(arr) - 1 - i]
		cur = mulit(c, cur)
		if cur == 'k' and lastk == -1:
			lastk = len(arr) - 1 - i
	return [cur], lastk

def judge(r1, r2, i, k, arr):
	#print r1, r2, i, k
	if i == -1 or k == -1:
		return False
	for i in xrange(i, k - 1):
		if r1[i] == 'i' and r2[i + 1] == 'i':
			print arr[:i + 1], arr[i + 1:k], arr[k:]
			return True
	return False

T, = R()
for c in xrange(1, T + 1):
	outp.write('Case #%d: ' % c)
	l,x, = R()
	seed, = SR()
	arr = ''
	for i in xrange(x):
		arr += seed

	r1,n1 = find_all_i(arr)
	r2,n2 = find_all_k(arr)
	print r1[-1], r2[0], n1, n2, n1 < n2, n1 != -1
	if r1[-1] == "-1" and (n1 < n2 and n1 != -1):
		outp.write('YES\n')
	else:
		outp.write('NO\n')
