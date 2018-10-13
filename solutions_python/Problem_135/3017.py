#!/usr/bin/python3

#import numpy

'''
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
'''

def main():
	f = open('../test_files/input', 'r')
	w = open('../test_files/output', 'w')
	s = f.readline()
	t = int(s)
	for i in range(1, t+1):
		w.write('Case #%d: ' % i)

		a1 = int(f.readline()[:-1])
		for i in range(a1-1):
			f.readline()
		row1 = [int(x) for x in f.readline()[:-1].split()]
		for i in range(4-a1):
			f.readline()

		a2 = int(f.readline()[:-1])
		for i in range(a2-1):
			f.readline()
		row2 = [int(x) for x in f.readline()[:-1].split()]
		for i in range(4-a2):
			f.readline()

		def find():
			answer = -2
			for d1 in row1:
				for d2 in row2:
					if d1 == d2:
						if answer != -2:
							return -1
						answer = d1
			return answer

		o = find()
		if o == -2:
			w.write('Volunteer cheated!')
		elif o == -1:
			w.write('Bad magician!')
		else:
			w.write(str(o))

		w.write('\n')

	w.close()

if __name__ == '__main__':
	main()