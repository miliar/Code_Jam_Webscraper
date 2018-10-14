from operator import itemgetter

def solve():
    d, n = map(int, input().split())
    h = [list(map(int, input().split())) for _ in range(n)]

    h.sort(key=itemgetter(0))
    #print(h)
    u = 0
    while len(h) > 1:
        m = 1000000000
        c = -1
        for i in range(len(h) - 1):
            if h[i][1] == h[i + 1][1]:
                continue
            t = (h[i + 1][0] - h[i][0]) / (h[i][1] - h[i + 1][1])
            if t > 0 and t < m:
                m = t
                c = i
        
        if c == -1:
            break

        if h[c][0] + h[c][1] * m > d:
            break

        h[c][0] += h[c][1] * m
        h[c][1] = min(h[c][1], h[c + 1][1])
        h.pop(c + 1)

        for i in range(len(h)):
            if i != c:
                h[i][0] += h[i][1] * m
        u += m

    #print(h)
    return d / ((d - h[0][0]) / h[0][1] + u)


t = int(input())
for i in range(t):
    print('Case #%d: %.6f' % (i + 1, solve()))