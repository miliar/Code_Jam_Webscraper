import sys
import math


def get_score(r, c, w):
    return c // w * r + w - 1 + int(c % w != 0)

def main():
    t = int(sys.stdin.readline())
    for k in range(t):
        r, c, w = map(int, sys.stdin.readline().split())
        print ('Case #%d: %d' % (k + 1, get_score(r, c, w)))

if __name__ == '__main__':
    main()
