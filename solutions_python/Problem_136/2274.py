#!/usr/bin/env python

import sys

def main():
	infile = open(sys.argv[1], 'r')
	outfile = open(sys.argv[2], 'w')

	num_case = int(infile.readline())
	case = 1
	for line in infile:
		print line
		line = map(float, line.split(' '))
		c = line[0]
		f = line[1]
		x = line[2]

		rate = 2
		t_farm = 0
		t_th = c / f + c / rate
		while True:
			if x / rate + t_farm > t_th:
				t_farm += c / rate
				rate += f
				t_th += c / rate
			else:
				break

		outstr = 'Case #{0}: {1:.7f}'.format(case, t_farm + x / rate)
		# print outstr
		outfile.write('{0}\n'.format(outstr))
		case += 1

	infile.close()
	outfile.close()


if __name__ == "__main__":
	main()