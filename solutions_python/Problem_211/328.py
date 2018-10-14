import sys, copy;
#from operator import itemgetter
def solve(n,k,u,pi):
    p = sorted(pi)
    #print n,p
    if u == 0:
        return probProduct(n,p)
    ph = calcPH(n,p)
    pn = calcPN(n,p)

    nx = 0;
    while u > 0.0000001:
        #print "ph:", ph
        #print "pn:", pn
        #print "p[0]]:", p[0]
        nn = ph[p[0]]
        nxt = pn[p[0]]
        ux=min(nn*(nxt-p[0]), u)
        #print "ux:",ux,'ux/n', ux/nn
        for j in range(0,nn):
            p[j]+=ux/nn
        u-=ux
        #print "u:",u
        if u == 0:
            break
        p = sorted(p)
        ph = calcPH(n,p)
        pn = calcPN(n,p)
        nx+=1

    res = probProduct(n,p);
    print "u:", u, "p:", p, "res:",res
    return res#probProduct(n,p)
def probProduct(n,p):
    pr = 1
    for i in range(0,n):
        pr *= p[i]
    return pr
def calcPH(n,p):
    ph = {}
    for i in range(0, n):
        if p[i] in ph:
            ph[p[i]]+=1
        else:
            ph[p[i]] = 1
    return ph

def calcPN(n,p):
    pn = {}
    current = None
    for i in range(0, n):
        if current == None:
            current = p[i]
        if p[i] > current:
            pn[current] = p[i]
            current = p[i]
    if not current in pn:
        pn[current] = 1
    return pn  
inputFile =  sys.argv[1] if (len(sys.argv) > 1) else "input.txt";
outputFile = sys.argv[2] if (len(sys.argv) > 2) else (inputFile + "out.txt") if (len(sys.argv) > 1) else "output.txt";
print(inputFile, outputFile)
file = open(outputFile, "w")

with open(inputFile, 'r') as f:
    t = int(f.readline())
    print(t)
    for i in range(1, t + 1):
        file.write("Case #" + str(i) + ": ")
        n,k=map(int,f.readline().split())
        u = float(f.readline())
        pi = map(float,f.readline().split())
        print i, n, k, u, pi
        file.write(str(solve(n,k,u,pi)) + "\n")
file.close()            








