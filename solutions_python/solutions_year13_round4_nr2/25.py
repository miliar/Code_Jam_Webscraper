import sys
sys.path.insert(0, '/home/rishig/codejam/')
from library import *

def digits(x):
    count = 0
    while x > 0:
        x = x//2
        count += 1
    return count

def solvecase(case):
    N,P = readints(f)

    # guaranteed
    maxlosses = N - digits(2**N-P)
    k = maxlosses
    guaranteed = min(2**(k+1)-2,2**N-1)

    # could
    reqwins = N+1 - digits(P)
    l = reqwins
    could = min(2**N-2**l,2**N-1)

    return '%s %s' % (guaranteed, could)


if __name__ == '__main__':
    f = file(sys.argv[1])
    T = readint(f)
    sys.stderr.write(strftime("%H:%M:%S\n"))
    for case in range(1,T+1):
        ans = solvecase(case)
        print 'Case #%d: %s' % (case, ans)
        if T <= 15 or case == 1 or case % max((T//10),5) == 0:
            sys.stderr.write('completed case %d, ' % case)
            sys.stderr.write(strftime("%H:%M:%S\n"))
