#!/usr/bin/python3
import numpy

def main():
	f = open('../test_files/input', 'r')
	w = open('../test_files/output', 'w')
	s = f.readline()
	t = int(s)
	for i in range(1, t+1):
		w.write('Case #%d: ' % i)
		n, m = [int(x) for x in f.readline()[:-1].split()]
		a = []
		for j in range(n):
			a.append([int(x) for x in f.readline()[:-1].split()])
		if solve(a):
			w.write("YES\n")
		else:
			w.write("NO\n")
	w.close()

def solve(a):
	a = numpy.array(a)
	while not 0 in a.shape:
		a1 = True
		a2 = True
		x = numpy.unravel_index(numpy.argmin(a), a.shape)
		c = a[:, x[1]]
		for d in c:
			if a[x[0], x[1]] != d:
				a1 = False
				break
		c = a[x[0], :]
		for d in c:
			if a[x[0], x[1]] != d:
				a2 = False
				break
		if not (a1 or a2):
			return False
		if (not a1) or (a1 and a2 and a.shape[0] < a.shape[1]):
			a = numpy.delete(a, x[0], 0)
		else:
			a = numpy.delete(a, x[1], 1)
	return True

if __name__ == '__main__':
	main()