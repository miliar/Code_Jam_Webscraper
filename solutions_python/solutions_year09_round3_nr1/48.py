T = int(raw_input())

for t in xrange(T):
    V = raw_input()
    D = {}
    Val = {}
    S = list(V)
    Val[S[0]] = 1
    D[S[0]] = 1
    S.pop(0)
    i = 0
    for c in S:
        if i==1: i+=1
        if c in D.keys():
            D[c] += 1
        else: D[c] = 1
        if c not in Val.keys():
            Val[c] = i
            i+=1
    
    base = len(D)
    if base <= 1: base = 2
    
    N = 0
    for c in V:
        N *= base
        N += Val[c]
    
    print "Case #"+str(t+1) + ": " + str(N)
