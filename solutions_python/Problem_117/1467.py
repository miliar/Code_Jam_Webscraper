
inputFile = 'input.txt'
inputFile = 'B-small-attempt0.in'
outputFile = 'output.txt'

f = open(inputFile, 'rb')
inputs = f.readlines()
f.close()

total = int(inputs[0])
count = 1
        
i = 1
result = ''

def isSquareOk(p, q, n, m, destPattern):
    maxR=0
    maxC=0
    for i in range (n):
        if destPattern[i][q] > maxR:
            maxR=destPattern[i][q]
    for i in range (m):
        if destPattern[p][i] > maxC:
            maxC=destPattern[p][i]

    if maxR > destPattern[p][q] and maxC > destPattern[p][q]:
        return 0
    if maxR > destPattern[p][q]:
        return 1
    if maxC > destPattern[p][q]:
        return 2
    return 3

def test(destPattern, count, n, m):
    isOk=[[0 for q in range(m)] for p in range(n)]
    for p in range(n):
        for q in range(m):
            isOk[p][q] = isSquareOk(p,q,n,m,destPattern)
            if isOk[p][q] == 0:
                return 'Case #%d: NO' %count

    isRowOk = [0 for p in range(n)]
    isColumnOk = [0 for p in range(m)]
    #print isOk
    for p in range(n):
        key = isOk[p][0]
        for q in range(m):
            #print p,q
            key = key & isOk[p][q]
        isRowOk[p] = key

    
    for q in range(m):
        key = isOk[0][q]
        for p in range(n):
            key = key & isOk[p][q]
        isColumnOk[q] = key

    for p in range(n):
        for q in range(m):
            if not isRowOk[p] and not isColumnOk[q]: 
                return 'Case #%d: NO' %count
            else:
                return 'Case #%d: YES' %count

while i < len(inputs):
    n, m=inputs[i].replace('\r','').replace('\n','').strip().split()
    n = int(n)
    m = int(m)
    destPattern = []
    for j in range(n):
        destPattern.append(inputs[i+1+j].replace('\r','').replace('\n','').strip().split())
        
    i=i+n+1
    result += test(destPattern, count, n, m) + '\r\n'
    count += 1

f=open(outputFile,'wb')
f.write(result)
f.close()
    
