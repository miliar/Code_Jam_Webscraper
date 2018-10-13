T = int(raw_input())

def conv(c):
    if c == '.':
        return -1
    elif c == '0':
        return 0
    else:
        return 1

for t in range(T):
    N = int(raw_input())
    res = []
    for i in range(N):
        res.append(map(conv,raw_input()))

    w = []
    l = []
    wp = []
    for i in range(N):
        w.append(1.0*res[i].count(1))
        l.append(1.0*res[i].count(0))
        wp.append(w[i]/(w[i]+l[i]))

    owp = []
    for i in range(N):
        a = []
        for j in range(N):
            if res[j][i] != -1:
                a.append( (w[j]-res[j][i])/(w[j]+l[j]-1) )
        owp.append(sum(a)/len(a)) 

    oowp = []
    for i in range(N):
        a = []
        for j in range(N):
            if res[j][i] != -1:
                a.append(owp[j])
        oowp.append(sum(a)/len(a))
    print "Case #%d:"%(t+1)

    for i in range(N):
        print 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]

