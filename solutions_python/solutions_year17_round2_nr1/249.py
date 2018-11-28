import sys

def solve(D, N, horses):
    tslowest = max(float(D - Ki) / Si for (Ki, Si) in horses)
    return D / tslowest


def main():
    T = int(sys.stdin.readline().strip())

    for i in xrange(T):
        D, N = map(int, sys.stdin.readline().split())
        horses = []
        for j in xrange(N):
            K, S = map(int, sys.stdin.readline().split())
            horses.append((K,S))
        ans = solve(D, N, horses)
        print 'Case #%s: %s' % (i+1, ans)

if __name__ == '__main__':
    main()
