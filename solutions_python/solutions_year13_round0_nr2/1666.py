__author__="reszegtivadar"
__date__ ="$Apr 14, 2012 12:49:51 AM$"

if __name__ == "__main__":
    print "Hello";


def findLocalMinimIndexes(arr):
    locMin = arr[0]
    indexes= []
    lastIndex = [0]
    
    
    for k in range(len(arr)):
        if (k > 0):
            if (arr[k] < locMin):
                locMin = arr[k]                
                lastIndex = [k]
                if (k == len(arr)-1):
                    indexes.append(k)
                    
            elif (arr[k] == locMin):
                lastIndex.append(k)
            elif (arr[k] > locMin):
                for o in range(len(lastIndex)):
                    indexes.append(lastIndex[o])
                lastIndex = []
                locMin = arr[k]
                
    if (not 0 in lastIndex):
        for o in range(len(lastIndex)):
            indexes.append(lastIndex[o])
            
    print "calculate for ",  arr,  " res",  indexes
    return indexes

def computeRes(N,  M,  matrAray):
    res = 'YES'
    if (N == 1 or M == 1):
        res = 'YES'
        return res
        
    localMinimRowIndexes = []
    for i in range(N):
        localMinimRowIndexes.append(findLocalMinimIndexes(matrAray[i]))
    localMinimColIndexes = []
    for j in range(M):
        columnj = []
        for i in range(N):
            columnj.append(matrAray[i][j])
        localMinimColIndexes.append(findLocalMinimIndexes(columnj))
        
    #print " sor index ",  localMinimRowIndexes
    #print " osz index ",  localMinimColIndexes
    
    for k in range(len(localMinimRowIndexes)):
        indRow = localMinimRowIndexes[k]
        for u in range(len(indRow)):
            colNr = indRow[u]
            
            canBeSourronded = False
            top = True
            right = True
            bottom = True
            left = True
            if (k > 0):
                if (matrAray[k][colNr] < matrAray[k-1][colNr]):
                    top = False
            if (k < len(matrAray)-1):
                if (matrAray[k][colNr] < matrAray[k+1][colNr]):
                    bottom = False
            if (colNr > 0):
                if (matrAray[k][colNr] < matrAray[k][colNr-1]):
                    left = False
            if (colNr < len(matrAray[k])-1):
                if (matrAray[k][colNr] < matrAray[k][colNr+1]):
                    right = False
                    
                    
                    
            #canBeSourronded = top and right and bottom and left
            #if (not canBeSourronded):
            if k in localMinimColIndexes[colNr]:
                res = "NO"
                return res
    return res



from textFile import TextFile
#input = TextFile('compete/B-test.in')
#output = TextFile('compete/B-test.out')

input = TextFile('compete/B-small-attempt5.in')
output = TextFile('compete/B-small-attempt5.out')

allLines = input.readLinesFromFileAsIntArray();
#print allLines
numberOfLines = allLines[0][0]
print numberOfLines

counter = 1
for i in range(numberOfLines):
    N = allLines[counter][0]
    M = allLines[counter][1]
    
    matrAray = []
    for k in range(N):
        counter += 1
        matrAray.append(allLines[counter])
    counter += 1
    #print N,  M,  matrAray
    print N,  M
    for te in range(len(matrAray)):
        print matrAray[te]
    
    
    res = computeRes(N,  M,  matrAray)
    print res
    
    printedLine = "Case #"+str(i+1)+": "+res+ "\n"
    print (printedLine )
    if (i == 0):
       output.writeToFile(printedLine)
    else:
       output.appendToFile(printedLine)

