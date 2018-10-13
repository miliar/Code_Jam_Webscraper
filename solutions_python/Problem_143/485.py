d = [[0 for i in range(1000)] for j in range(1000)]
with open('d.in') as f:
    for line in f:
        k = line.split()
        a = int(k[0])
        b = int(k[1])
        d[a][b] = int(k[2])
with open('blpp.in') as f:
    data = [line.rstrip() for line in f]
i = 1
ncase = 1
while i < len(data):
    print "Case #%d:" % ncase,
    a, b, c = [int(j) for j in data[i].split()]
    cc = 0
    for k in range(a):
        for j in range(b):
            if d[k][j] < c:
                cc += 1
    print cc
    i += 1
    ncase += 1