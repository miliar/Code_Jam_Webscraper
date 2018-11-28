C = int(raw_input())

for c in xrange(1, C+1):
    #print "GAR", raw_input()
    
    #print " ".split(raw_input().strip())
    
    N, M = map(int, raw_input().split())
    
    exists = [raw_input() for i in xrange(N)]
    need = [raw_input() for i in xrange(M)]
    
    #print exists, need
    
    d = {}
    
    for s in exists:
        s_split = s[1:].split('/')
        
        acc = ""
        for ss in s_split:
            acc += ss + "/"
            #print acc
            d[acc] = True
        
        
    ans = 0
    
    for s in need:
        s_split = s[1:].split('/')
        
        acc = ""
        for ss in s_split:
            acc += ss + "/"
            #print acc
            
            if acc not in d:
                ans += 1
                d[acc] = True
                
    print "Case #%d: %d" %(c, ans)