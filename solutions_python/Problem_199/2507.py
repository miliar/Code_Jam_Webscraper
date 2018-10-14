
from __future__ import division
import sys
import math

input = open('input.in')
output = open('out', 'wb')


class gcj:
    IN = input
    number = 0

    @classmethod
    def case(cls):
        cls.number += 1
        return 'Case #%d: ' % cls.number

    @classmethod
    def line(cls, type=str):
        line = cls.IN.readline()
        return type(line.strip('\n'))

    @classmethod
    def split_line(cls, type=str):
        line = cls.IN.readline()
        # print line
        return [type(x) for x in line.split()]

def solve(pancake, flip):
	ret = 0
	flip = int(flip)
	pancake = list(pancake)
	for i in xrange(len(pancake)):
		if pancake[i] == '+':
			continue
		if len(pancake)-i < flip:
			return 'IMPOSSIBLE'
		# flip
		ret += 1
		for j in xrange(flip):
			pancake[i+j] = '+' if pancake[i+j] == '-' else '-'
        return ret

def main():
    t = gcj.line(int)

    for i in xrange(t):
        pancake, flip = gcj.split_line()
        output.write(gcj.case() + str(solve(pancake,flip)) + '\n')

    input.close()
    output.close()


if __name__ == '__main__':
    main()
