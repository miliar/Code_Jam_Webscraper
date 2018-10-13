import string

def isPossible(lawn,x,y):
    allRow = []
    allCol = []
    mx = -2
    for k in range(x):
        aRow = lawn[k].split(' ')
        hldRow = []
        for h in range(y):
            ht = int(aRow[h])
            if ht > mx: mx = ht
               
            hldRow.append(ht)
            if k == 0:
                allCol.append([ht])
            else:
                allCol[h] = allCol[h] + [ht]
        allRow.append(hldRow)
    for k in range(x):
        for h in range(y):
            ht = allRow[k][h]
            if ht < mx:
                col = allCol[h]
                row = allRow[k]
                if max(col) != min(col) and max(row) != min(row):
                    return 'NO'
    return 'YES'


inFile = open('B-small-attempt0.in','r')
outPut = open('lawmower1.in','w')
inPut = inFile.read()
inPut = inPut.split('\n')
T = int(inPut[0])

Cases = inPut[1:]
emt = Cases.count('')
for h in range(emt):
    Cases.remove('')
for k in range(1,T+1):
    xy = Cases[0].split(' ')
    x = int(xy[0])
    y = int(xy[1])
    lawn = Cases[1:x+1]
    outPt = isPossible(lawn,x,y)
    outPut.write('Case #%d:' % (k) + " "+outPt+'\n')
    Cases = Cases[x+1:]
        
inFile.close()
outPut.close()
