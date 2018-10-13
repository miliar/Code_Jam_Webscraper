import sys

v0 = 2.0

def whenFaster(C,v0,vInc):
    tmp = C/vInc
    return [tmp,v0*tmp]


def calcT(C,F,X):
    n0 = int(X/C-v0/F)
    if n0 <0:
        return X/v0
    T = X/(v0+n0*F)+C*sum(map(lambda k:1/(v0+k*F),range(n0)))
    return T


def calcLine(line):
    tmp = line.split(" ")
    C = float(tmp[0])
    F = float(tmp[1])
    X = float(tmp[2])
    return calcT(C,F,X)

def getData(fileName):
    f = open(fileName, 'r+')
    lines = [line for line in f]
    nCases = int(lines[0])
    lines = lines[1:]
    k = 1
    while k <= nCases:
        tmp = lines[0]
        lines = lines[1:]
        print "Case #"+str(k)+": "+str(calcLine(tmp))
        k = k+1

getData(sys.argv[1])
