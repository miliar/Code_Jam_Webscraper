import sys

def rl():
    return sys.stdin.readline().strip()

def main():
    fas = [int(d) for d in (str(i**2) for i in xrange(1, 10**7+1) if str(i) == str(i)[::-1]) if d == d[::-1]]
    T = int(rl())
    for i in range(1, T+1):
        A, B = map(int, rl().split())
        print 'Case #{}: {}'.format(i, len([x for x in fas if A <= x <= B]))

if __name__ == '__main__':
    main()
