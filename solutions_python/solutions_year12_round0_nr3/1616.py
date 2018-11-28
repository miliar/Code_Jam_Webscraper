theFile = open("csmall.txt")
A = 0
B = 0
pairsDict = {}
    
def findPossiblePairs(givenRange):
    for i in givenRange:
        strinRepOfDigit = str(i)
        pairs = []
        leng = len(strinRepOfDigit)
        for j in range(1, leng):
            strinRepOfDigit = strinRepOfDigit[-j:] + strinRepOfDigit[0:leng-j] 
            pairs.append(int(strinRepOfDigit))
            strinRepOfDigit = str(i)
        pairsDict[i] = pairs
    

def checkResults(results):
    valid = []
    results = list(set(results)) #remove duplicates
    for i in range(len(results)):
        #results[i] = int(results[i]) #remove all leading zeros
        res = set() #following logic removes all of the same number eg 33333
        for j in str(results[i]):
            res.add(j)
        if len(res) == 1:
            results[i] = 0
    
    for j in results: #now all integers
        #print j, A, B
        if (j >= A) and (j <= B): #checks they're in range
            valid.append(j)
        
    for k in valid:
        if len(str(k)) != len(str(A)): #checks they're the right lenght
            valid.remove(k)        
    return valid   

def getpairCount(pairDict):
    keys = pairDict.keys()
    keys.sort()
    count = 0
    for n in keys:
        mList = pairDict[n]
        
        new = []
        for m in mList:
            if m > n:
                new.append(m)
        new = checkResults(new)
       
                
        count += len(new)
        pairDict[n] = new
        
        if new == []:
            pairDict.pop(n)
        

    return count 
    
    
while 1:
    try:
        numTestCases = int(theFile.readline())
    except:
        break
    for i in range(numTestCases):
        line = theFile.readline()
        if not line:
            break
        linelst = line.split()
        A = int(linelst[0])
        B = int(linelst[1])
        inRange = range(A, B+1, 1)
        findPossiblePairs(inRange)
        num = getpairCount(pairsDict)
        
        pairsDict = {}
        

        ans = "Case #%d: " % (i+1) + str(num)
        num = 0
        print ans
