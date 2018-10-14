def mdc(a,b):
    if b == 0:
        return a
    else:
        return mdc(b,a%b)

C = int(raw_input())

for caso in range(1,C+1):
    s = raw_input()
    S = s.split(' ')
    N = int(S[0])
    g = []

    for i in range(0,N):
        g.append(int(S[i+1]))

    m = []

    for i in range(0,N):
        for j in range(i+1,N):
            m.append(abs(g[i]-g[j]))

    T = m[0];
    for x in m:
        T = mdc(T,x)

    y = T-(g[0]%T)
    if y == T:
        y = 0

    print "Case #%d: %d" % (caso,y)

