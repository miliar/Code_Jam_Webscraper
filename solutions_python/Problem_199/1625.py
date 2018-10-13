numcases = input()
for i in range(numcases):
    s,k = raw_input().split()
    k = int(k)
    s = map(lambda c:c=="+",s)
    c = 0
    for j in range(len(s)-k+1):
        if not s[j]:
            c+=1
            for l in range(j,j+k):
                s[l]=not s[l]
    for j in s[-k+1:]:
        if not j:
            print "CASE #%d: IMPOSSIBLE"%(i+1)
            break
    else:
        print "CASE #%d: %d"%(i+1,c)
            
        
    