# Copy method
import copy

# Optimal War
def wo(nao, ken):
    nao = copy.copy(nao)
    ken = copy.copy(ken)
    point = 0
    # Loop
    while len(nao) and len(ken):
        if nao[0] > ken[0]:
            point += 1
            nao.pop(0)
            ken.pop(len(ken)-1)
        else:
            nao.pop(0)
            ken.pop(0)
    return point

# Optimal Deceiptful
def do(nao, ken):
    nao = copy.copy(nao)
    ken = copy.copy(ken)
    point = 0
    # Loop
    while len(nao) and len(ken):
        if nao[len(nao)-1] < ken[len(ken)-1]:
            nao.pop(len(nao)-1)
            ken.pop(0)
        else:
            nao.pop(len(nao)-1)
            ken.pop(len(ken)-1)
            point += 1
    return point

f = open( "D-large.in", "r" )
out = open( "D_large.out", "w")
N = int(f.readline())

for n in xrange(1,N+1):
    T = int(f.readline())
    na = sorted(map(float, f.readline().split(" ")), reverse=True)
    ke = sorted(map(float, f.readline().split(" ")), reverse=True)
    # Problem solution
    wp = wo(na,ke)
    dp = do(na,ke)
    out.write("Case #%d: %d %d\n" % (n, dp, wp))

f.close()
out.close()
    
