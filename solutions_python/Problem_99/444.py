__author__ = 'alei'
def solve(A,B,probs):
    nCols = 2**A
    nRows = 3+A
    #m = [[0]*(nCols + 1)]*(nRows)
    m=[]
    for i in range(nRows):
        m.append([0]*(nCols + 1))

    binario = [0]*A

    colIndex = 0
    onEnter = B+2
    for i in range(nCols):
        prob = calcProb(binario,probs)
        ceroRow = m[0]
        ceroRow[colIndex]=prob
        nEntersKT = 0
        if 0 in binario:
            nEntersKT = 2*B-A+2
        else:
            nEntersKT = B - A + 1
        (m[1])[colIndex] = nEntersKT
        (m[2])[colIndex] = onEnter
        for nbacks in range(1,A+1):
            if 0 in binario[0:len(binario)-nbacks]:
                nEnters = B-A+nbacks+1 + B + 1 +nbacks
            else:
                nEnters = B-A+nbacks+1 + nbacks
            (m[2+nbacks])[colIndex] = nEnters
        sumaUno(binario)
        colIndex+=1

    minXp = -1
    for i in range(1,nRows):
        xp = 0
        for j in range(nCols):
            xp+=m[0][j]*m[i][j]
        if minXp==-1:
            minXp = xp
        else:
            minXp = min(minXp,xp)
    return minXp


def calcProb(binario,probs):
    prob = 1
    nDigit = 0
    for digit in binario:
        if digit==0:
            prob*=1-probs[nDigit]
        else :
            prob *=probs[nDigit]
        nDigit+=1
    return prob

def sumaUno(binario):
    nDigit = len(binario)-1
    while binario[nDigit]==1:
        binario[nDigit] = 0
        nDigit-=1
    binario[nDigit] = 1

f = open("A.in","r")
w = open("A.out","w")
nCases = int(f.readline())
for i in range(nCases):
    A,B = [int(x) for x in f.readline().split()]
    probs = [float(x) for x in f.readline().split()]
    n = solve(A,B,probs)
    w.write("Case #{0}: {1}\n".format(i+1,n))
f.close()
w.close()