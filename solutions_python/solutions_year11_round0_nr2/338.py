T = int(raw_input())
for caso in range(T):
    line = raw_input().split()
    
    comb = list()
    opp = list()
    
    n = int(line[0])
    comb = line[1:n+1]
    line = line[n+1:]
    n = int(line[0])
    opp = line[1:n+1]
    line = line[n+2:][0]
    
    res = ""
    for c in line:
        res += c
        if len(res) < 2:
            continue
        
        t = res[-2]
        
        done = False
        
        #~print res
        
        for a in comb:
            if a.startswith(t+c) or a.startswith(c+t):
                res = res[:-2] + a[2]
                done =True
                break
        
        if done:
            continue
        
        #~print opp
        
        for t in res:
            if t == c:
                continue
            #~print "chars: ",t,c
            if (t+c) in opp or (c+t) in opp:
                res = ""
                break
    out = "["
    for i in range(len(res)):
        if i > 0:
            out += ", "
        out += res[i]
    out += "]"
            
    
    print 'Case #%s:'%(caso+1), out
    
