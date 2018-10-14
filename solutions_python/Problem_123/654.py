#!/usr/local/bin/python3 -tt
import sys

def main():
	fl = open('A-small-attempt9.in','r')
	w = open('A-small-attempt9.out','w')
	t = int(fl.readline())
	for case in range(t):
		status = solvecase(fl)
		w.write('Case #' + str(case + 1) + ': ' + status + '\n')

def solvecase(fl) :
	an = fl.readline().split()
	a = int(an[0])
	n = int(an[1])
	spores = fl.readline().split()
	for i in range(n):
		spores[i] = int(spores[i])
	spores.sort()
	if a == 1 and spores[0] == 1:
		return str(n)
	count = 0
	for i in range(n):
		if spores[i] < a:
			a += spores[i]
		else :
			if i == n - 1:
				return str(count + 1)
			else:
				x = 1
				while (2**x*a-(2*(2**(x-1))-1)) <= spores[i] and x < n - i:
					x+=1
				if x == n - i:
					return str(count + n - i)
				else :
					a = 2**x*a-(2*(2**(x-1))-1) + spores[i]
					count += x
	return str(count)

	

if __name__ == '__main__':
	main()
