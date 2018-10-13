import sys

def war(n, k, s):
    r = 0
    np = s - 1
    kp = s - 1
    for i in range(s):
        if n[np] > k[kp]:
            r += 1
            np -= 1
            kp -= 1
        else:
            kp -= 1
    return r
    

filename = sys.argv[1]
outputfile = "warresult"

fi = open(filename, 'r')
fo = open(outputfile, 'w')

caseNum = int(fi.readline())
for i in range(caseNum):
    pileSize = int(fi.readline())
    NaomiPile = [float(item) for item in fi.readline().split(' ')]
    KenPile = [float(item) for item in fi.readline().split(' ')]
    NaomiPile.sort()
    KenPile.sort()
    warScore = pileSize - war(KenPile, NaomiPile, pileSize)
    dwarScore = war(NaomiPile, KenPile, pileSize)
    fo.write( "Case #{0}: {1} {2}\r\n".format(i+1, dwarScore, warScore))
    
