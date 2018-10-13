#
#python 2.6


INPUT_FILE = 'C-large.in'
OUT_FILE = 'C-large.out'
rf = file(INPUT_FILE)
wf = file(OUT_FILE, 'w')

caseNum = 0
def inputs():
    global caseNum
    if caseNum == 0:
        caseNum = rf.readline().strip()
        caseNum = int(caseNum)
    for i in xrange(caseNum):
        strarray = rf.readline().strip().split()
        R, K, N = [long(num) for num in strarray]
        strarray = rf.readline().strip().split()
        groups = [long(num) for num in strarray]
        yield R, K, groups

def getNextIndex(i, totalLen):
    if i == totalLen-1:
        return 0
    else:
        return i+1
    

def computey(R, K, groups):
    #(r, index) -> y
    cacheI2RY = {}
    
    r = 0
    y = 0
    currTailIndex = len(groups)-1
    
    while r < R:
        oldTailIndex = currTailIndex
        if cacheI2RY.has_key(currTailIndex):
            oldr, oldy = cacheI2RY[currTailIndex]
            quotient, remainder = divmod(R-r, r-oldr)
            y += quotient*(y-oldy)
            r += quotient*(r-oldr)
            if r == R:
                break
        
        sum = 0
        
        if len(groups) == 1:
            sum = groups[0]
        else:
            i = getNextIndex(currTailIndex, len(groups))
                
            while True:
                sum += groups[i]
                if sum > K:
                    sum -= groups[i]
                    break
                currTailIndex = getNextIndex(currTailIndex, len(groups))
                if i == oldTailIndex:
                    break
                i = getNextIndex(i, len(groups))
        cacheI2RY[oldTailIndex] = (r, y)
        y += sum
        r += 1
                
    return y

caseIndex = 1
for R, K, groups in inputs():
    wf.write('Case #%d: %s\n' %(caseIndex,computey(R,K,groups))) 
    caseIndex += 1

print 'Done'
wf.close()
rf.close()
