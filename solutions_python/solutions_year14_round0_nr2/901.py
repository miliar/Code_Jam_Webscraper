inputFile = open('B-large.in','r')
outputFile = open('B-large.ou','w')


numTest = int(inputFile.readline())
for testid in range(1,numTest+1):
    line = inputFile.readline()
    CFX = [float(x) for x in line.split()]
    C = CFX[0]
    F = CFX[1]
    X = CFX[2]

    n = 0
    T0 = 0
    Tmin = X/2
    Tn = T0 + X/2
    while Tn<=Tmin+1e-12:
        Tmin = Tn
        n = n + 1
        T0 = T0 + C/(2+(n-1)*F)        
        Tn = T0 + X/(2+n*F)

    print('Case #',testid,': ',Tmin, sep='',file=outputFile)

outputFile.close()
