import fractions
f = open("data.txt")
g = open("data1.txt", 'w')
j = int(f.readline())
for i in range(1, j+1):
    h = f.readline()
    h = list(h.partition(' '))
    n = int(h.pop(0))
    del h[0]
    m = []
    for r in range(n-1):
        h = list(h[0].partition(' '))
        m.append(int(h.pop(0)))
        del h[0]
    m.append(int(h[0]))
    m.sort()
    md = []
    for r in range(n-1):
        md.append(m[r+1] - m[r])
    t = md[-1]
    for r in range(n-2):
        t = fractions.gcd(md[r], t)
    y = (t - (m[0]%t))%t
    string = 'Case #'+str(i)+": "+str(y)+'\n'
    g.write(string)
