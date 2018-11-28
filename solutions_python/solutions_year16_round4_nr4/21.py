import sys
import random


def check(a):
	n = len(a)
	b = [None] * n
	c = [None] * n
	for i in range(n):
		if b[i] is not None:
			continue
		jj = None
		for j in range(n):
			if a[i][j] == 1:
				jj = j
				break
		for j in range(n):
			if a[i][j] == 1:
				c[j] = 1
		if jj is None:
			return False
		ws = [ii for ii in range(n) if a[ii][jj] == 1]
		for x in ws:
			if a[x] != a[i]:
				return False
		if len(ws) != len([1 for j in range(n) if a[i][j] == 1]):
			return False
		for x in ws:
			b[x] = 1
	if len([1 for x in c if x is None]) != 0:
		return False
	return True


def allenum2(n, i):
	if i == 0:
		yield []
		return
	if len(n) < i:
		return
	for x in allenum2(n[1:], i-1):
		yield [n[0]] + x
	for x in allenum2(n[1:], i):
		yield x



def allenum(n):
	for i in range(n*n+1):
		for x in allenum2(list(range(n*n)), i):
			yield x


def check2(a, x):
	n = len(a)
	for y in x:
		if a[y//n][y%n] == 1:
			return False
	return True

def add(a, x):
	n = len(a)
	res = [a[i][:] for i in range(n)]
	for y in x:
		res[y//n][y%n]  = 1
	return res

def foo(ifile):
	n = int(ifile.readline())
	a = [[int(x) for x in list(ifile.readline().strip())] for i in range(n)]
	for x in allenum(n):
		#print x
		if not check2(a, x):
			continue
		if check(add(a, x)):
			return len(x)
	return "ERROR"


def main():
    ifile = sys.stdin
    n = int(ifile.readline())
    for i in range(n):
        print 'Case #%d: %s' % (i+1, foo(ifile))
        sys.stdout.flush()

main()

