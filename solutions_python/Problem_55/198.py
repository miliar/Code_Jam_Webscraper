from fractions import gcd

def ThemePark(R,k,N, G, u):
    total = 0
    playing = []
    for i in range(R):
        tt = 0
        while len(G)>0 and tt+G[0]<=k:
            tmp = G.pop(0)
            tt += tmp
            playing.append(tmp)
        total += tt
        for j in range( len(playing) ):
            G.append( playing.pop(0) )
    return "Case #%d: %d\n" % (u, total)


fp = open("C-small-attempt0.in", 'r')
fout = open("C-small-attempt0.out", 'w')
T = int(fp.readline())
for i in range(1, T+1):
    R,k,N = fp.readline().split()
    R  = int(R)
    k = int(k)
    N = int(N)
    g = fp.readline().split()
    for j in range(0, len(g)):
        g[j] = int(g[j])
    fout.write(ThemePark(R,k,N, g, i))
fp.close()
fout.close()

