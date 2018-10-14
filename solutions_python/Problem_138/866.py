##inputFile = open('D-small-practice.in','r')
##outputFile = open('D-small-practice.ou','w')
##inputFile = open('D-small-attempt2.in','r')
##outputFile = open('D-small-attempt2.ou','w')
inputFile = open('D-large.in','r')
outputFile = open('D-large.ou','w')
def winsinWar(N,K):
    if len(N)==1:
        if N[0]<K[0]:
            return 0
        else:
            return 1
    i = 0
    j = 0
    wincount = 0
    while (i<len(N) and j<len(K)):
        if N[i]<K[j]:
            i = i+1
            j = j+1
        elif N[i]>K[j]:            
            while (j<len(K) and K[j]<N[i]):
                j = j+1
                wincount = wincount+1
            if (j<len(K)):
                i = i+1
                j = j+1           
        
    return wincount


def winsinDeceitfulWar(N,K):
    if len(N)==1:
        if N[0]<K[0]:
            return 0
        else:
            return 1
    i = 0
    j = 0
    wincount = 0
    while (i<len(N)):
        if N[i]>K[j]:
            j = j+1
            wincount = wincount+1
        i = i+1
    return wincount

numTest = int(inputFile.readline())
for testid in range(1,numTest+1):
    numblks = int(inputFile.readline())
    
    N = [float(x) for x in inputFile.readline().split()]
    K = [float(x) for x in inputFile.readline().split()]
    N.sort()
    K.sort()
##    print(numblks)
##    print('N',N)
##    print('K',K)


    print('Case #',testid,': ',winsinDeceitfulWar(N,K),' ',winsinWar(N,K), sep='',file=outputFile)

outputFile.close()
