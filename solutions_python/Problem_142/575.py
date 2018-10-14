fi = open('in.txt', 'r')
fo = open('out.txt', 'w')

import math

def create(s):
	n = len(s)
	t = ""
	t+=s[0]
	for i in range(n-1):
		if s[i+1]!=s[i]:
			t+=s[i+1]
	return t

def match(s1, s2):
	if create(s1) == create(s2):
		return 1
	else:
		return 0

def makearr(seq, s):
	m, n = len(seq), len(s)
	i, j, count = 0, 0, 0
	a = []
	while j!=n:
		if seq[i] != s[j]:
			i+=1
			a.append(count)
			count = 0
		else:
			j+=1
			count+=1
	a.append(count)
	return a

def rnd(x):
	if x - math.floor(x) >= 0.5:
		return math.floor(x) + 1
	else:
		return math.floor(x)

def mean(a):
	n, m = len(a), len(a[0])
	r = []
	for j in range(m):
		sum = 0.0
		for i in range(n):
			sum+=a[i][j]
		sum/=n
		r.append(rnd(sum))
	return r

def fn():
	n = int(fi.readline())
	s, a = [], []
	for i in range(n):
		tmp = fi.readline()
		s.append(tmp)
	seq = create(s[0])
	flag = 1
	for i in range(n-1):
		if match(seq, s[i+1]) == 0:
			flag = 0
	if flag==0:
		fo.write("Fegla Won\n")
		return
	if flag != 0:
		for i in range(n):
			a.append(makearr(seq, s[i]))
	b = mean(a)
	moves = 0
	m = len(b)
	for i in range(n):
		for j in range(m):
			moves+= abs(a[i][j] - b[j])
	fo.write(str(int(moves)))
	fo.write("\n")

t = int(fi.readline())
for i in range(t):
	fo.write("Case #")
	fo.write(str(i+1))
	fo.write(": ")
	fn()

