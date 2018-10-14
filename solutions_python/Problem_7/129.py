import pickle

def input(file):
    
    params = [ int(a) for a in file.readline().split() ]
    
    x = []
    y = []

    n = params[0]
    A = params[1]
    B = params[2]
    C = params[3]
    D = params[4]
    X = params[5]
    Y = params[6]
    M = params[7]
    
    x.append(X)
    y.append(Y)
    #print X, Y
 
    for i in xrange(1, n):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        
        #print X, Y
        
        x.append(X)
        y.append(Y)
    
    return (x, y)

def solve():
    fileName = "C:\A"
    fileIn = open(fileName + ".in")
    fileOut = open(fileName + ".out", 'w')
    
    T = int(fileIn.readline())
    
    for i in xrange(0, T):
        (x, y) = input(fileIn)
        #s1 = {}, s2 = {}, s3 = {}
        remX = [set(), set(), set()]
    
        for r in xrange(0, len(x)):
            remX[x[r] % 3].add((x[r], y[r]))
            
        print remX[0]
        print remX[1]
        print remX[2]
    
        result = set()
            
        for r1 in xrange(0, 3):
            for r2 in xrange(r1, 3):
                r3 = ((6 - r1 - r2) % 3)
                if (r3 >= r2):
                    for (x1, y1) in remX[r1]:
                        for (x2, y2) in remX[r2]:
                            if ((x1, y1) != (x2, y2)):
                                for (x3, y3) in remX[r3]:
                                    if ((x1, y1) != (x3, y3)):
                                        if ((x3, y3) != (x2, y2)):
                                            if (0 == (y1 + y2 + y3) % 3):
                                                X = sorted([x1, x2, x3])
                                                Y = sorted([y1, y2, y3])
                                                result.add((X[0], X[1], X[2], Y[0], Y[1], Y[2]))
                                    
        outStr = "Case #" + str(i + 1) + ": " + str(len(result)) + "\n"
        fileOut.write(outStr)

solve()