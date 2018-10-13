#coding: utf-8
#!/usr/bin/env python2.7
import sys
import copy

def main():
	line = []
	for l in sys.stdin: line.append(l)

	counter = 0
	num = int(line[counter][:-1])
	counter += 1

	for i in range(1, num+1):
		C, F, X = map(float, line[counter][:-1].split())
		counter += 1

		best_time = X/2
		sum_time = 0
		N = 0

		while 1:
			sum_time += C/(2+F*N)
			last_time = X/(2+F*(N+1))
			if sum_time + last_time < best_time:
				best_time = sum_time + last_time
			else:
				break
			N += 1
		print 'Case #%s: %.7f' % (str(i), best_time)
		
if __name__ == '__main__':
	main()
