import sys
from collections import defaultdict
# sys.stdin = open('c1.in')
sys.stdin = open('C-small-attempt0.in')
# sys.stdin = open('C-large.in')
sys.stdout = open('out.txt', 'w')




def solve_it():
    n, q = list(map(int, input().split()))
    e = []
    s = []
    for i in range(n):
        _e, _s = list(map(int, input().split()))
        e.append(_e)
        s.append(_s)
    d = []
    for i in range(n):
        d.append(list(map(int, input().split())))
    inf = 10 ** 30
    dist = [[inf] * n for i in range(n)]
    for k in range(n):
        dist[k][k] = 0
    for i in range(n):
        for j in range(n):
            if d[i][j] != -1:
                dist[i][j] = d[i][j]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    u = [list(map(int, input().split())) for i in range(q)]
    res = 0
    best = [0] * n
    reach = [inf] * n
    reach[0] = 0
    for i in range(n):
        for j in range(i):
            if dist[j][i] <= e[j]:
                t = reach[j] + dist[j][i] / s[j]
                if t < reach[i]:
                    reach[i] = t
    res = reach[n - 1]
    return res

def main():

    n_cases = int(input())
    for test_case in range(1, n_cases + 1):
        print(test_case, file=sys.stderr, end=' ')
        res = solve_it()
        print('Case #' + str(test_case) + ':', res)

    print(file=sys.stderr)

if __name__ == '__main__':
    main()
