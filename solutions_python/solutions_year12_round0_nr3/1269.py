#!/usr/bin/env python

import sys

def main():
    n = int(sys.stdin.readline())
    for i in range(1, n+1):
        line = sys.stdin.readline()[:-1]

        print 'Case #{0}: {1}'.format(i, recycled_numbers(line))

def recycled_numbers(line):
    split = line.split(" ")
    a = int(split[0])
    b = int(split[1])

    pairs = []

    ret = 0

    for n in range(a, b+1):
        if n % 10000 == 0:
            print n
        recycled = RNumber(n)
        for m in recycled:
            if a <= m and n < m and m <= b and (n, m) not in pairs:
                pairs.append((n, m))
                ret += 1


    return ret

class RNumber:
    def __init__(self, n):
        self.numstr = str(n)
        self.index = 1

    def __iter__(self):
        return self

    def next(self):
        while (self.index < len(self.numstr)):
            self.__tempstr = self.numstr[self.index:] + self.numstr[:self.index]
            self.index += 1
            if self.__tempstr[0] != '0':
                return int(self.__tempstr)
        raise StopIteration


if __name__ == '__main__':
	main()
