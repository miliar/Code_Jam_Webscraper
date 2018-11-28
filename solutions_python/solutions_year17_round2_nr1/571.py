from __future__ import print_function
from sys import stderr

def eprint(*args):
    print(*args, file=stderr)

def makeAnswer(i, answers):
    return ('Case #%d: ' % (i+1)) + '\n'.join(answers)

def solve(i):
    dest, n = [int(s) for s in raw_input().split()]
    horses = []
    for h in xrange(n):
        pos, speed = [int(s) for s in raw_input().split()]
        horses.append((pos, float(speed)))

    maxArrival = 0.0
    horses.sort(lambda x, y: -1 if x[0] > y[0] else 1)
    for horse in horses:
        left = dest - horse[0]
        arrival = left / horse[1]
        if arrival > maxArrival:
            maxArrival = arrival

    # should return list of strings
    return ['%.6f' % (dest/maxArrival)]

if __name__ == '__main__':
    numCases = int(raw_input())

    # calculate
    solutions = (solve(i) for i in xrange(numCases))

    # print
    print('\n'.join((makeAnswer(i, solution) for i, solution in enumerate(solutions))))
