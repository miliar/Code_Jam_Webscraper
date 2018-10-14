def readInts():
    r = raw_input()
    s = r.split()
    if len(s) == 1:
        return int(s[0])
    return [int(ss) for ss in s]

def readString():
    r = raw_input()
    return r


def main():
    t = readInts()
    
    case = 1
    for i in xrange(t):

        r = readInts()
        brd = {}
        brd2 = {}
                
        for rr in xrange(r):
            x1, y1, x2, y2 = readInts()
            
            if x1 > x2:
                x1, x2 = x2, x1
            
            if y1 > y2:
                y1, y2 = y2, y1
                
            for x in xrange(x1, x2 + 1):
                if not brd.has_key(x):
                    brd[x] = {}
                        
                for y in xrange(y1, y2 + 1):
                    brd[x][y] = 1

        count = 0
        while True:
            for k in brd:
                x = k
                for y in brd[x]:
                    if brd[x].has_key(y - 1) or brd.has_key(x - 1) and brd[x - 1].has_key(y):
                        if not brd2.has_key(x):
                            brd2[x] = {}
                        brd2[x][y] = 1
                    
                    if brd.has_key(x - 1) and brd[x - 1].has_key(y + 1):
                        if not brd2.has_key(x):
                            brd2[x] = {}
                        brd2[x][y + 1] = 1

            count += 1
            if not brd2:
                break

            brd = brd2
            brd2 = {}

        print 'Case #%d: %d' % (case, count)
        case += 1

if __name__ == '__main__':
    main()

