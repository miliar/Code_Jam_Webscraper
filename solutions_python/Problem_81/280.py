f = open("g_A.in","r")
f2 = open("g_A.out","w")
T = int(f.readline().strip())

def solve(n,tb):
    r = [0]*n
    wp = [0]*n
    owp = [0]*n
    oowp = [0]*n
    ops = []
    for el, i  in zip(tb,xrange(n)):
        tmp = []
        for j in xrange(n):
            if (el[j] != "."):
                tmp.append(j)
        ops.append(tmp)

    for i in xrange(n):
        wp[i] = sum(map(lambda x:int(tb[i][x]),ops[i]))/float(len(ops[i]))
        owp[i] = 0.0
        for j in ops[i]:
            k = ops[j]+[]
            k.remove(i)
            owp[i] += sum(map(lambda x:int(tb[j][x]),k))/float(len(k))
        owp[i]/=float(len(ops[i]))

    for i in xrange(n):
        oowp[i] = sum( map(lambda x:owp[x],ops[i]))/ float(len(ops[i]))
        r[i] = 0.25 * wp[i] + 0.5 * owp[i] + 0.25*oowp[i]

    
    return r

for t in xrange(1, T+1):
    table = []
    N = int(f.readline().strip())
    for n in xrange(N):
        table.append(f.readline().strip())

    out = solve(N,table)
    f2.write( "Case #%d:\n" % (t) )
    for i in out:
        f2.write( "%.8f\n" % (i) )


f2.close()

f.close()
