def trans(i):
    if i == '+':
        return True
    if i == '-':
        return False
        

T = input()

for case in xrange(1,T+1):
    S,K = raw_input().split()
    K = int(K)

    ans = 0
    
    happy = [trans(i) for i in S]
    
    for i in range(len(S)-(K-1)): #len(S) == K ==> 1 #correct
        if not happy[i]: # flip
            ans += 1
            for j in range(i,i+K):
                happy[j] = not happy[j]
        else: # no flip
            pass
            

    for i in range(len(S)-(K-1),len(S)):
        if not happy[i]:
            ans = False
            break
            
        
    
    if ans is not False:
        print "Case #%d: %d" % (case,ans)
    else:
        print "Case #%d: %s" % (case,"IMPOSSIBLE")
