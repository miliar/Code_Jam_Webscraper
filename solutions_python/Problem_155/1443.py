import numpy
from sys import stdin

def solve(line):
    Smax, data = line.split()
    data = [int(x) for x in data]
    cusum = numpy.cumsum(data)
    return max([i-x if i-x > 0 else 0 for i, x in enumerate(cusum, start=1)])

if __name__ == '__main__':
    T = int(stdin.readline())
    for case, line in enumerate(stdin.readlines(), start = 1):
        answer = solve(line)
        print "Case #%d: %s" % (case, answer)
