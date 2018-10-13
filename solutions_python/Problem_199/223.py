import sys

def solve():
    S, K = sys.stdin.readline().rstrip().split()
    K = int(K)

    l = len(S)
    s = [1 if i == '-' else 0 for i in S]

    csum = 0
    old = 0

    for i in range(0, l):
        csum -= old
        s[i] = (csum + s[i]) % 2
        csum = (csum + s[i]) % 2

        if i >= K-1:
            old = s[i-K+1]

    for i in range(l-K+1, l):
        if s[i]:
            return 'IMPOSSIBLE'
            break
    else:
        return sum(s)

def main():
    T = int(sys.stdin.readline().rstrip())
    for t in range(1, T+1):
        answer = solve()
        print 'Case #{}: {}'.format(t, answer)

if __name__ == "__main__":
    main()
