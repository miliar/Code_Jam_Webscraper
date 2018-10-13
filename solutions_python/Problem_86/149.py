import sys

def main():    
    cases = int(raw_input())
    
    for c in xrange(1, cases+1):
        N, L, H = map(int, raw_input().split())
        others = map(int, raw_input().split())
        
        note = "NO"
        for i in xrange(L, H+1):
            note = i
            allPass = True
            for j in others:
                if note%j != 0 and j%note != 0:
                    allPass = False
                    break
                    
            if allPass:
                break
                
        if allPass:
            result = str(note)
        else:
            result = "NO"
        #print N, L, H
        #print others
        #result = 
        print "Case #%d: %s"%(c, result)
        #print >> sys.stderr, "Case #%d: %d"%(c, result)
        
if __name__ == '__main__':
    main()
