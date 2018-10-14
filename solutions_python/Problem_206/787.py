import sys

def solve():
    [d, n] = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    best = 0
    for _ in xrange(n):
        [k,s] = [float(x) for x in sys.stdin.readline().strip().split(' ')]
        time = (d-k)/s
        best = max(best, time)
    return d / best



def main():
    T = int(sys.stdin.readline().strip())
    for i in xrange(T):
        res = solve()
        print('Case #{}: {}'.format(i+1, res))

if __name__ == '__main__':
    main()
