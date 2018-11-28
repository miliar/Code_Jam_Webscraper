T = int(raw_input())

for c in range(1, T + 1):
    R, k, N = map(int, raw_input().split())
    gs = map(int, raw_input().split())
    
    riding = k
    start = currentInd = 0 
    for i in range(len(gs)):
        if(riding >= gs[i]):
            riding -= gs[i]
        else:            
            start = i
            break
        
    money = [k - riding]
    
    if start != 0:
        currentInd = start  
        for r in xrange(R - 1):
            riding = k
            begin = currentInd
            while riding >= gs[currentInd]:
                riding -= gs[currentInd]
                currentInd = (currentInd + 1) % len(gs)
                if currentInd == begin: break
                
            money.append(k - riding)                
            if currentInd == start or currentInd == 0:
                break
    
    #print money, start, currentInd
    total = 0    
    
    if currentInd != 0:
        total = money[0]
        money = money[1:]
        R -= 1
        
    if len(money) > 0:
        total += R / len(money) * sum(money)
        total += sum(money[:R % len(money)])
            
    print "Case #%d: %s" % (c, total)
