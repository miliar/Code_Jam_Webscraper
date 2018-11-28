
inFile = open("intput1.txt", "r")
outFile = open("output1.txt", "w")
    
def solve1(X, S, R, t, N, B, E, w):
    #print (X,S,R,t,N,B,E,w)
    tLeft = t
    curX = 0
    res = 0.0
    cIndex = 0
    
    while cIndex < N:
        tmpRT = (B[cIndex] - curX) / R
        if tmpRT > tLeft:
            res += tLeft
            res += (B[cIndex] - curX - tLeft * R) / S
            tLeft = 0
        else:
            res += tmpRT
            tLeft -= tmpRT
        
        tmpRT = (E[cIndex] - B[cIndex]) / (R + w[cIndex])
        if tmpRT > tLeft:
             res += tLeft
             res += (E[cIndex] - B[cIndex] - tLeft * (R + w[cIndex])) / (w[cIndex] + S)
             tLeft = 0
        else:
             res += tmpRT
             tLeft -= tmpRT
            
        curX = E[cIndex]
        cIndex += 1
    
    tmpRT = (X - curX) / R
    if tmpRT > tLeft:
         res += tLeft
         res += (X - curX - tLeft * R) / S
         tLeft = 0
    else:
         res += tmpRT
         tLeft -= tmpRT
    
    return res;

def solve2(X, S, R, t, N, B, E, w):   
    res = 0
    tLeft = t
    curX = 0
    
    for cIdx in range(N):
        tmpRT = (B[cIdx] - curX) / R
        if tmpRT > tLeft:
            res += tLeft
            res += (B[cIdx] - curX - tLeft * R) / S
            tLeft = 0
        else:
            res += tmpRT
            tLeft -= tmpRT
    
        curX = E[cIdx]
    
    tmpRT = (X - curX) / R
    if tmpRT > tLeft:
         res += tLeft
         res += (X - curX - tLeft * R) / S
         tLeft = 0
    else:
         res += tmpRT
         tLeft -= tmpRT
    
    
    sortW = list(w)
    sortW.sort()
    maxW = max(sortW)
    mW = sortW.pop(0)
    while True:
        for cIdx in range(N):
            if w[cIdx] == mW:
                tmpRT = (E[cIdx] - B[cIdx]) / (R + w[cIdx])
                if tmpRT > tLeft:
                     res += tLeft
                     res += (E[cIdx] - B[cIdx] - tLeft * (R + w[cIdx])) / (w[cIdx] + S)
                     tLeft = 0
                else:
                     res += tmpRT
                     tLeft -= tmpRT
        if mW == maxW :
            break;
        newmW = sortW.pop(0)
        while  newmW == mW and len(sortW) > 0 :
            newmW = sortW.pop(0)
        mW = newmW
        
    return res
        
    
N = int(inFile.readline())
for case in range(1, N + 1):
    llLine = inFile.readline().split()
    
    X = int(llLine[0])
    S = int(llLine[1])
    R = int(llLine[2])
    t = int(llLine[3])
    N = int(llLine[4])
    B = []
    E = []
    w = []
    
    for i in range(N):
        llLine = inFile.readline().split()
        B.append(int(llLine[0]))
        E.append(int(llLine[1]))
        w.append(int(llLine[2]))
    
    result = solve2(X, S, R, t, N, B, E, w)
    
    resStr = "Case #" + str(case) + ": "
    resStr = resStr + "%.8f" % result + "\n"
    print (resStr)
    outFile.write(resStr)
    
