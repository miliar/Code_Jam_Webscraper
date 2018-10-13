nc = int(raw_input())
for ic in xrange(nc):
    np,nk,nl = map(int,raw_input().split())
    messages = map(int,raw_input().split())
    #messages.sort(key=operator.itemgetter(1), reverse=True)
    messages.sort(reverse=True)
    
    
    #ans = None
    if np*nk < nl:
        ans = "Impossible"
    else:
        ans = 0
        i = 0
        while messages != []:
            i += 1
            for j in xrange(nk):
                ans += messages[0]*i
                messages.pop(0)
                if messages == []:
                    break
                
    print "Case #%s: %s" % (ic+1,ans)
                
                 
        
    