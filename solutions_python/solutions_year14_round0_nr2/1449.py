# 16:43

import math
import Queue
import copy

def solve():
	return 'result'

def main():
	# fp = open('b.in')
	# fp = open('B-small-attempt0.in')
	fp = open('B-large.in')
	# fp = open('A-small-practice.in')
	# fp = open('A-large-practice.in')

	for case in xrange(int(fp.readline())):
		c,f,x = fp.readline().split()
		c,f,x = float(c), float(f), float(x)
		
		# print c,f,x

		taxa = 2.0
		v = x / taxa
		demora = 0.0
		while demora < x:
			demora += c / taxa

			# print 'prox farm:', c / taxa,

			taxa += f

			# print '- demora acc:', demora, '- rest:', x / taxa, '- total:', demora + x / taxa

			if demora + x / taxa < v:
				v = demora + x / taxa
			else:
				break

		result = solve()

		print 'Case #{:n}: {:.7f}'.format(case+1, v)

		# break

if __name__ == "__main__":
	main()
