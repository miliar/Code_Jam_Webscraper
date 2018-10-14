import fractions
f = open("data.txt")
g = open("data1.txt", 'w')
j = int(f.readline())
for i in range(1, j+1):
    h = f.readline()
    h = h.partition(' ')
    r = int(h[0])
    h = h[-1].partition(' ')
    k = int(h[0])
    n = int(h[-1])
    m = []
    h = f.readline()
    h = h.partition(' ')
    m.append(int(h[0]))
    if n > 1:
        for s in range(n-2):
            h = h[-1].partition(' ')
            m.append(int(h[0]))
        m.append(int(h[-1]))
    income = 0
    for s in range(r):
        rc = []
        while (m != []) & ((sum(rc) + sum(m[:1])) < k+1):
            rc.append(m[0])
            del m[0]
        income += sum(rc)
        m = m + rc
    string = 'Case #'+str(i)+": "+str(income)+'\n'
    g.write(string)
