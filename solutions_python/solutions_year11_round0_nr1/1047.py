from sys import *
           
def getNextItem(items, i, X):
    for j in range(i, len(items)):
        if items[j][0] == X:
            return items[j]
    return None
def solve(_, items):
    num = 0
    c = int(items[0])
    items = [[items[i], int(items[i+1])] for i in range(1, c * 2, 2)]
    posO, posB = 1, 1
    for i in range(len(items)):
        #print posO, posB, num
        X, pos = items[i]
        if X == 'O':
            inc = abs(pos - posO) + 1
            num += inc
            posO = pos
            item = getNextItem(items, i, 'B')
            if item != None:
                X1, pos1 = item
                if pos1 != posB:
                    #inc = abs(pos - posO) + 2
                    if pos1 > posB:
                        right = True
                    else:
                        right = False
                    if right:
                        posB += inc
                        if posB > pos1:
                            posB = pos1
                    else:
                        posB -= inc
                        if posB < pos1:
                            posB = pos1
        else:
            inc = abs(pos - posB) + 1
            num += inc
            posB = pos
            item = getNextItem(items, i, 'O')
            if item != None:
                X1, pos1 = item
                if pos1 != posO:
                    #inc = abs(pos - posB) + 2
                    if pos1 > posO:
                        right = True
                    else:
                        right = False
                    if right:
                        posO += inc
                        if posO > pos1:
                            posO = pos1
                    else:
                        posO -= inc
                        if posO < pos1:
                            posO = pos1
                            
    print "Case #%d: %d" %(_+1, num)
    return
    
cases = int(raw_input())
for _ in xrange(cases):
    items = stdin.readline()[:-1].split(' ')
    solve(_, items)
