import sys

def getSingle(i, l):
    for x in l:
        if int(x) > i: return False
    return True

def getColumn(listOfLists, colNum):
    col = []
    for x in range(len(listOfLists)):
        col.append(listOfLists[x][colNum])
    return col
                   
    
def run():
    t = int(raw_input())
    for x in range(t):
        POSSIBLE = True
        n, m = raw_input().split(' ')
        n, m = int(n), int(m)
        data = []
        for y in range(n):
            data.append(raw_input().split(' '))

        for j in range(len(data)):
            for i in range(len(data[j])):
                if not getSingle(int(data[j][i]), data[j]):
                    col = getColumn(data, i)
                    if not getSingle(int(data[j][i]), col):
                        POSSIBLE = False
        if POSSIBLE == False:
            print 'Case #%d: NO' % (x + 1)
        else:
            print 'Case #%d: YES' % (x + 1)
    return


                
if __name__ == "__main__":
    run()
    sys.exit(0)
        
##l = []
##l.append([2, 2, 2, 2, 2])
##l.append([2, 1, 1, 1, 2])
##l.append([2, 1, 2, 1, 2])
##l.append([2, 1, 1, 1, 2])
##l.append([2, 2, 2, 2, 2])
##print l
##print getColumn(l, 0)
##print getColumn(l, 2)


    
    
    
        
    
