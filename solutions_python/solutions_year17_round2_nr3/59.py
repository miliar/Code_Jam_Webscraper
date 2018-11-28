import sys

def floyd(g, n):
    inf = 2000000000*1000
    
    r = [[inf]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if g[i][j] != -1 and g[i][j] != inf:
                r[i][j] = g[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if r[i][k] + r[k][j] < r[i][j]:
                    r[i][j] = r[i][k] + r[k][j]

    return r
    
    
def gao(T):
    n, q = map(int, raw_input().split())
    es = [map(int, raw_input().split()) for i in range(n)]
    g = [map(int, raw_input().split()) for i in range(n)]
    uv = [map(int, raw_input().split()) for i in range(q)]
    inf = 2000000000*1000

    # print T
    
        
    road = floyd(g, n)
    t = [[inf]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            t[i][j] = inf
            if road[i][j] <= es[i][0]:
                t[i][j] = float(road[i][j]) / es[i][1]
    t = floyd(t, n)

    # print t
    ans = []
    for i in range(q):
        # print uv[i]
        ans.append(t[uv[i][0] - 1][uv[i][1] - 1])

    return ans

    
def run(T):
    ans = gao(T)
    for i in ans:
        print "%.6f" % (i),
    print ''
    
def main():
    T = input()
    for cas in range(1, T+1):
        print "Case #%d:" % (cas),
        run(cas)

if __name__ == '__main__':
    sys.stdin = open("C-large.in", "r")
    sys.stdout = open ("cout.txt", "w")
    main()
