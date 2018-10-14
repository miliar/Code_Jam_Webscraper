import sys

def solve(N, n, k):
    n.sort()
    k.sort()
    k_war = 0
    k_d_war = 0
    war_score = 0
    d_war_score = 0
    for i in range(N):
        nv = n[i]
        while k_war < N and k[k_war] < nv:
            k_war += 1
        if k_war == N:
            war_score += 1
        else:
            k_war += 1
        if k[k_d_war] < nv:
            d_war_score += 1
            k_d_war += 1
    return "%d %d" % (d_war_score, war_score)

def main():
    T = int(sys.stdin.readline())
    for t in range(T):
        N = int(sys.stdin.readline())
        n = map(float, sys.stdin.readline().split())
        k = map(float, sys.stdin.readline().split())
        result = solve(N, n, k)
        print "Case #%d: %s" % (t + 1, result)

if __name__ == '__main__':
    main()
