#!/usr/bin/python

def main():
    N = 2000000
    count = {}
    for n in range(1, N+1):
        count[n] = {}
        n_str = str(n)
        sz = len(n_str)
        for r in range(1, sz):
            if n_str[0] <= n_str[r]:
                m = int(n_str[r:] + n_str[0:r])
                if m > n and m <= N:
                    # print n, m
                    count[n][m] = True

    T = int(raw_input())
    for t in range(1, T+1):
        ans = 0
        inp = raw_input().split()
        A = int(inp[0])
        B = int(inp[1])
        for n in range(A, B+1):
            ans += len(filter(lambda x: x<=B, count[n].keys()))
        print "Case #" + str(t) + ": " + str(ans)

if __name__ == '__main__':
    main()
