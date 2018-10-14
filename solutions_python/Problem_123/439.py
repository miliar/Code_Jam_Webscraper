from __future__ import print_function
import unittest
import sys
import math

sin = '''5
2 2
2 1
2 4
2 1 1 6
10 4
25 20 9 100
1 4
1 1 1 1
4 3
8 12 13'''

def err(*msgs, **argv):
    print(*msgs, file=sys.stderr, **argv)

def getMax(A, m):
    if A == 1:
        return 10 ** 7
    result = int(math.ceil(math.log(1.0 * m / (A - 1), 2)))
    return result


def solveCase(A, N, motes):
    motes = sorted(motes)
    count = 0
    upper = len(motes)
    for i in range(len(motes)):
        m = motes[i]
        if A > m:
            A += m
            continue
        MAX = getMax(A, m)
        if MAX <= len(motes) - i:
            A = (2 ** MAX) * (A - 1) + 1 + m
            err('MAX', MAX, 'A is now', A)
            count += MAX
        else:
            err('remove', m)
            count += 1
    if count > upper:
        count = upper
    return count

def solveAll(s):
    it = iter(s.split('\n'))
    T = int(it.next())
    for i in range(T):
        A, N = map(int, it.next().split(' '))
        motes = map(int, it.next().split(' '))
        assert len(motes) == N
        # Add the additional last vines with l=0
        yield('Case #%s: %s' % (i + 1, solveCase(A, N, motes)))

def test():
    #print('\n'.join(solveAll(sin)))
    #print(solveCase(2, 4, [2,1,1,6]))
    #print(solveCase(10, 4, [25, 20, 9, 100]))
    print(solveCase(4, 3, [8, 12, 13, 200]))

if __name__ == '__main__':
    if 'test' in sys.argv[1:]:
        test()
        sys.exit(0)
    print('\n'.join(solveAll(open('alarge.in').read())))
