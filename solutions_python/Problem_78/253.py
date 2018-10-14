import sys

def main():    
    cases = int(raw_input())
    
    for c in xrange(1, cases+1):
        N, D, G = map(int, raw_input().split())
        
        result = 'Broken'
        
        if G == 100 and D < 100 or G == 0 and D > 0:
            result = 'Broken'
        else:        
            for i in xrange(1, N+1):
                if i*D % 100 == 0:
                    result = 'Possible'
                    #print i
                
        #result = 
        print "Case #%d: %s"%(c, result)
        #print >> sys.stderr, "Case #%d: %d"%(c, result)
        
if __name__ == '__main__':
    main()
