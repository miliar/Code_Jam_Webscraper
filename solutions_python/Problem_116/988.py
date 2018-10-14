#!/usr/bin/python

fin = open('A-large.in')
fout = open('large.out', 'w')
num = int(fin.readline())
l=1

def checksub(a):
	count = [0, 0, 0];
	for i in a:
		if i == '.':
			return 0
		if i == 'O':
			count[0] += 1;
		elif i == 'X':
			count[1] += 1;
		elif i == 'T':
			count[2] += 1;
	if count[0] + count[2] == 4:
		return 'O won\n'
	elif count[1] + count[2] == 4:
		return 'X won\n'
	return 0


def check(a, b, c):
	for i in a:
		ans = checksub(i)
		if ans:
			return ans
	for i in b:
		ans = checksub(i)
		if ans:
			return ans
	for i in c:
		ans = checksub(i)
		if ans:
			return ans
	return 0


while(l<=num):
	n = 0
	a = []
	b = [[],[],[],[]]
	c = [[],[]]
	flag = 0
	while (n<4):
		d = list(fin.readline())
		a.append(d[:4])
		m = 0
		while (m<4):
			b[m].append(d[m])
			if not flag and d[m] == '.':
				flag = 1
			m += 1
		c[0].append(d[3-n])
		c[1].append(d[n])
		n += 1
	pre = 'Case #'+str(l)+': '
	ans = check(a, b, c)
	if ans :
		ans = pre+ans
	else:
		if flag:
			ans = pre+'Game has not completed\n'
		else:
			ans = pre+'Draw\n'
	fout.write(ans)
	fin.readline()
	l += 1