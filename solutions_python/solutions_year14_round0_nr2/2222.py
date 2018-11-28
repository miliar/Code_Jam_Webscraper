import os
import sys

if __name__ == '__main__':
	f = open('input.txt')
	numCases = -1
	case = 0
	for line in f:
		if numCases == -1:
			numCases = int(line)
		else:
			case += 1
			splitted= line.strip().split()
			#: C, F and X,
			c = float(splitted[0])
			f = float(splitted[1])
			x = float(splitted[2])
			minT = 100000000
			sum = 0
			for k in range(0,1000000):
				if k > 0:
					sum += c/(f*(k-1)+2)
				r = x/(2.0+f*k)
				t = sum+r
				if t < minT:
					minT = t
				else:
					break
			print 'Case #{0}: {1}'.format(case, minT)