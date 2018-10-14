from collections import deque
import sys

filename = sys.argv[1]

f = open('%s.in' % filename)
g = open('%s.out' % filename, 'w')

DEBUG = sys.argv[2] if len(sys.argv) >= 3 else False
def dlog(s, *n):
    if DEBUG:
        if n:
            print(s % tuple(n))
        else:
            print(s)

def solve(n):
    dlog(n)
    i = first_bad(n)
    dlog(i)
    if i is None:
        return n
    first = solve(str(int(line[:i+1]) - 1))
    second = '9' * (len(n) - i - 1)
    return first + second

def first_bad(n):
    for i in range(len(n) - 1):
        if int(n[i]) > int(n[i+1]):
            return i
    return None

T = int(f.readline())
for t in range(T):
    dlog("Case %d", t)
    line = f.readline().strip()

    g.write('Case #%d: %d' % ((t + 1), int(solve(line))))
    g.write('\n')


