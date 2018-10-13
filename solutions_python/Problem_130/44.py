def prizes(N, P):
    if P == (2**N):
        return (P-1, P-1)
    
    prizeString = str(bin(2**N - P))
    prizeString = prizeString[2:]
    prizeString = '0'*(N-len(prizeString)) + prizeString

    numWins = 0
    for i in range(len(prizeString)):
        if prizeString[i] == '1':
            numWins += 1
        else:
            if int(prizeString[i:]) != 0:
                numWins += 1
            break

    worstPossible = (2**N - 1) - (2**(numWins) - 1)

    firstWin = prizeString.find('1')
    bestRequired = (2**(firstWin+1)-1-1)

    return (bestRequired, worstPossible)
    

    
filename = "B-large (5).in"
outputname = filename + 'out.txt'

inFile = open(filename, 'r')
outFile = open(outputname, 'w')

numTests = int(inFile.readline())

for i in range(numTests):
    test = inFile.readline().split()
    N = int(test[0])
    P = int(test[1])
    res = prizes(N,P)
    outFile.write("Case #" + str(i+1) + ": " + str(res[0]) + ' ' + str(res[1]) + '\n')
    print "Case #" + str(i+1) + ": " + str(res[0]) + ' ' + str(res[1]) + '\n'
    
inFile.close()
outFile.close()
