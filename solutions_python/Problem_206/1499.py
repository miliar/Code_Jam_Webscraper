for _ in range(int(raw_input())):
    d, n = map(int,raw_input().split())
    a = []
    for i in range(n):
        k, s = map(int,raw_input().split())
        a.append((k, s))
    a.sort(cmp=lambda x, y: y[0] - x[0])
    maxt = (d - a[0][0]) / float(a[0][1])
    for i in range(1, len(a)):
        if a[i][1] <= a[i - 1][1] or (a[i - 1][0] - a[i][0]) / float(a[i][1] - a[i - 1][1]) > maxt:
            maxt = max(maxt, (d - a[i][0]) / float(a[i][1]))
    print "Case #%d: %.9lf" %((_+1),d/float(maxt))
