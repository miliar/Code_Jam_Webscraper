

name = None
nVal = None

def solve():
    global name, nVal
    
    lastCheckpoint = 0
    sol = 0
    
    for i in xrange(len(name)):
        dim = len(name)-i
        if dim < nVal: break
        skip = False
        for q in xrange(i, i+nVal):
            if name[q] == 'a' or name[q] == 'e' or name[q] == 'i' or name[q] == 'o' or name[q] == 'u':
                skip = True
                break
        
        if not skip:
            #print name[i:(i+nVal)]
            Ssx = i-lastCheckpoint
            Sdx = len(name)-i-nVal
            #print '<%d, %d> = %d'  % (Ssx, Sdx, (Ssx+1)*(Sdx+1))
            sol += (Ssx+1)*(Sdx+1)
            
            lastCheckpoint = i+1
    return sol
            

def main():
    global name, nVal
    
    cases = int(input())
    for c in xrange(cases):
        name, nVal = raw_input().split()
        nVal = int(nVal)
        print 'Case #%d: %d' % (c+1, solve())


main()