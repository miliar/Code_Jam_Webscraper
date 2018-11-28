import fileinput

infile = fileinput.input()

T = int(infile.readline().strip())

c = {}

for l in range(T):
    N = infile.readline().strip()
#    print N
    c = {}
    t = []
    j = 0
    for i in range(len(N)):
        if N[i] in c.keys():
            t.append(c[N[i]])
        elif len(c) < 2:
            if j == 0:
                c[N[i]] = 1
                j = 1
                t.append(1)
                continue
            if j == 1:
                c[N[i]] = 0
                j = 2
                t.append(0)
                continue
        else:
            c[N[i]] = j
            t.append(j)
            j += 1

    b = len(c.keys())
    if b < 2:
        b = 2
    ti = 0
    for k in range(len(t)):
        ti = (b*ti) + t[k]
#    print t,ti,b
#    print ti, c, t
    print 'Case #%d: %d' % (l+1,ti)

infile.close()            