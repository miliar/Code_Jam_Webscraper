import sys

T = int(sys.stdin.readline())

for i in range(T):
    n = int(sys.stdin.readline())
    d = []
    l = []
    path = False
    for j in range(n):
        a, b = [int(w) for w in sys.stdin.readline().split()]
        d.append(a)
        l.append(b)
    D = int(sys.stdin.readline())
    gdl = []
    gdl.append((0,d[0]*2))
    if (d[0]*2 >= D):
        path = True
    else:
        for j in range(1,n):
            best = -1
            for k in reversed(gdl):
                if (k[1] < d[j]):
                    break
                diff = d[j] - d[k[0]]
                best = d[j] + min(l[j], diff)
                if (diff >= l[j]):
                    break
            if (best > gdl[-1][1]):
                gdl.append((j,best))
            if (best >= D):
                path = True
                break
    answer = "NO"
    if (path):
        answer = "YES"
    print("Case #%s: %s" % (str(i+1),answer))
