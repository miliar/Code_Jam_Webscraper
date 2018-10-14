import sys
from datetime import datetime


def debug(x):
    sys.stderr.write('{} DEBUG: {}\n'.format(datetime.now().time(), x))


def solve(D, N):
    pos = [0]*N
    speed = [0]*N
    maxt = 0.
    for i in xrange(N):
        pos[i], speed[i] = map(int, raw_input().split())
        maxt = max(maxt, float(D-pos[i])/float(speed[i]))
    return float(D)/maxt


def main():
    T = int(raw_input())
    for tc in xrange(1, T+1):
        D, N = map(int, raw_input().split())
        debug("Running test #{}...\n".format(tc))
        print "Case #{}: {:.8f}".format(tc, solve(D, N))


if __name__ == "__main__":
    main()
