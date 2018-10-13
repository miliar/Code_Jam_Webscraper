
def wf(fileName,ls):
    f = open(fileName,'w')
    for i,l in enumerate(ls):
        f.write('Case #%d:\n'%(i+1))
        l = [' '.join(x) for x in l]
        l = '\n'.join(l)
        f.write('%s\n'%l)

def flowTo(lsAltitude, lsBasin, r, c, ascii):
    #print 'to:',r,c,lsAltitude[r][c],len(lsAltitude),len(lsAltitude[0])
    hasMin,minR,minC,minV = getMinNeighbour(lsAltitude,lsBasin,r,c)
    
    if hasMin and not lsBasin[minR][minC]:
        #print hasMin
        lsBasin[minR][minC] = ascii
        flowTo(lsAltitude, lsBasin, minR, minC, ascii)
        flowFrom(lsAltitude, lsBasin, minR, minC, ascii)
   
def flowFrom(lsAltitude, lsBasin, r, c, ascii):
    #print 'from:',r,c,lsAltitude[r][c],len(lsAltitude),len(lsAltitude[0])
    hasMin,minR,minC,minV = getMinNeighbour(lsAltitude,lsBasin,r+1,c)
    if hasMin and minV==lsAltitude[r][c] and minR==r and minC==c:
        lsBasin[r+1][c] = ascii
        flowFrom(lsAltitude, lsBasin, r+1, c, ascii)
    
    hasMin,minR,minC,minV = getMinNeighbour(lsAltitude,lsBasin,r-1,c)
    if hasMin and minV==lsAltitude[r][c] and minR==r and minC==c:
        lsBasin[r-1][c] = ascii
        flowFrom(lsAltitude, lsBasin, r-1, c, ascii)

        
    hasMin,minR,minC,minV = getMinNeighbour(lsAltitude,lsBasin,r,c+1)
    if hasMin and minV==lsAltitude[r][c] and minR==r and minC==c:
        lsBasin[r][c+1] = ascii
        flowFrom(lsAltitude, lsBasin, r, c+1, ascii)
        
    
    hasMin,minR,minC,minV = getMinNeighbour(lsAltitude,lsBasin,r,c-1)
    if hasMin and minV==lsAltitude[r][c] and minR==r and minC==c:
        lsBasin[r][c-1] = ascii
        flowFrom(lsAltitude, lsBasin, r, c-1, ascii)
    
    
def getMinNeighbour(lsAltitude, lsBasin, r, c):
    
    if r<0 or c<0 or r>=len(lsAltitude) or c>=len(lsAltitude[0]):
        return False,0,0,0
    
    #print 'getMinNeighbour:',r,c,lsAltitude[r][c],len(lsAltitude),len(lsAltitude[0])
    hasMin = False
    minR = 0
    minC = 0
    minV = lsAltitude[r][c]
    
    
    if (r-1)>=0:
        if lsAltitude[r-1][c]<minV:
            hasMin = 'n'
            minR = r-1
            minC = c
            minV = lsAltitude[r-1][c]
    if (c-1)>=0:
        if lsAltitude[r][c-1]<minV:
            hasMin = 'w'
            minR = r
            minC = c-1
            minV = lsAltitude[r][c-1]
    if (c+1)<len(lsAltitude[0]):
        #print lsAltitude[r][c+1],minV
        if lsAltitude[r][c+1]<minV:
            hasMin = 'e'
            minR = r
            minC = c+1
            minV = lsAltitude[r][c+1]
    if (r+1)<len(lsAltitude):
        #print  lsAltitude[r+1][c],minV
        if lsAltitude[r+1][c]<minV:
            hasMin = 's'
            minR = r+1
            minC = c
            minV = lsAltitude[r+1][c]
            
    return hasMin,minR,minC,minV


f = open('Large.in')
contents = f.readlines()
n = int(contents[0].strip())
cur = 1

lsResult = []
for i in range(n):
    print i
    hw = contents[cur].split()
    cur += 1
    h = int(hw[0])
    w = int(hw[1])
    ls = []
    for r in range(h):
        ls.append( [int(x) for x in contents[cur].split() if x] )
        cur += 1
    
    arr = []
    for l in ls:
        a = []
        for c in l:
            a.append(False)
        arr.append(a)
    
    ascii = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
        's','t','u','v','w','x','y','z'
    ]
    curAscii = 0
    arr[0][0] = ascii[curAscii]
    flowTo(ls,arr,0,0,ascii[curAscii])
    flowFrom(ls,arr,0,0,ascii[curAscii])
    curAscii += 1
    while True:
        for ri,rv in enumerate(ls):
            for ci,cv in enumerate(rv):
                #print arr[ri][ci],cv
                if not arr[ri][ci]:
                    arr[ri][ci] = ascii[curAscii]
                    flowTo(ls,arr,ri,ci,ascii[curAscii])
                    flowFrom(ls,arr,ri,ci,ascii[curAscii])
                    curAscii += 1
        else:
            break
        
    lsResult.append(arr)

wf('x.out',lsResult)