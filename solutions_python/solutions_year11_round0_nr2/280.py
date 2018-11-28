#!/usr/bin/env python
fin = open('b.in', 'r')
fout = open('b.out', 'w')
n = 0
a = []
m = 0
b = []
s = ''
def main():
	global fin, fout, n, a, b, m, s
	T = int(fin.readline())
	for test in range(T):
		ax = fin.readline().split()
		n = int(ax[0]); ax = ax[1:]
		a = []
		for i in range(n):
			a.append(ax[0]); ax = ax[1:]
		m = int(ax[0]); ax = ax[1:]
		b = []
		for i in range(m):
			b.append(ax[0]); ax = ax[1:]
		s = ax[1]
		solve(test, s, a, b)

def solve(test, s, a, b):
	global fout
	sol = []
	for c in s:
		if len(sol) == 0:
			sol.append(c)
		else:
			sol.append(c)
			found = 1
			while len(sol) > 1 and found == 1:
				found = 0
				for v in a:
					if (v[0] == sol[-1] and v[1] == sol[-2]) or \
						(v[0] == sol[-2] and v[1] == sol[-1]):
						sol.pop(); sol.pop()
						sol.append(v[2])
						found = 1
						break
			found = 0
			for p in b:
				for i in range(len(sol)):
					for j in range(len(sol)):
						if i != j:
							if (p[0] == sol[i] and p[1] == sol[j]) or \
								(p[1] == sol[i] and p[0] == sol[j]):
								found = 1
			if found == 1:
				sol = []
	ss = ''
	ss +=  'Case #' + str(test + 1) + ': ['
	if len(sol) == 0:
		ss += ']'
	else:
		for i in sol:
			ss += str(i) + ', '
		ss = ss[:-2]
		ss += ']'
	fout.write(ss + '\n')  
		   
main()
