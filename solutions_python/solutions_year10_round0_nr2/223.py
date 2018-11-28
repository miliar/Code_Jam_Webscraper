import sys

def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a%b)

Tx = sys.stdin.readline()
T = int(Tx)
C = 1
while T > 0:
    linha = sys.stdin.readline()
    linhas = linha.split()
    n = int(linhas[0])
    v = []
    for i in range(1,n+1):
        v.append(int(linhas[i]))
    v.sort()
    t = v[1]-v[0]
    for i in range(2,n):
        t = mdc(t, v[i]-v[i-1])
    resp = t*((v[0]+t-1) / t) - v[0]
    print "Case #"+str(C)+": "+str(resp)
    C = C + 1
    T = T - 1
