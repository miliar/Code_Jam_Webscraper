s = [0 for i in range(31)]
ns = [0 for i in range(31)]
for a in range(11):
    for b in range(max(a-2,0),min(a+3,11)):
        for c in range(max(a-2,b-2,0), min(a+3,b+3,11)):
            if(abs(a-b) == 2 or abs(b-c) == 2 or abs(a-c) == 2):
                s[a+b+c] = max(max(a,b,c),s[a+b+c])
            else:
                ns[a+b+c] = max(max(a,b,c),ns[a+b+c])
T = int(raw_input())
for Ti in range(1,T+1):
    l = raw_input().split()
    N = int(l[0])
    S = int(l[1])
    p = int(l[2])
    totals = [int(l[i]) for i in range(3,len(l))]
    sCount = 0
    nsCount = 0
    for t in totals:
        if (ns[t] >= p):
            nsCount += 1
        elif (s[t] >= p):
            sCount += 1
    print "Case #%d: %d" % (Ti, nsCount + min(sCount,S))
    
    

