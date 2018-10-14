ip = open("A-large.in", "r")
a = ip.readlines()
NoOfTestCases = int(a[0])
curline = 0
for i in range(NoOfTestCases):
    curline += 1
    curinp = a[curline]
    n = int(curinp)
    curline += 1
    curinp = a[curline]
    xs = curinp.split()
    curline += 1
    curinp = a[curline]
    ys = curinp.split()
    x = []
    y = []
    for j in range(n):
        x += [int(xs[j])]
        y += [int(ys[j])]
    x.sort()
    y.sort()
    y.reverse()
    sp = 0
    for j in range(n):
        sp += x[j] * y[j]
    print "Case #%d: %d" % (i+1, sp)
    
