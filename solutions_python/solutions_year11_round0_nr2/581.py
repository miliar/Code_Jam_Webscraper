T = int(raw_input())

for i in range(T):
    dat = raw_input().split()

    C = int(dat[0])
    clis = dat[1:1+C]
    D = int(dat[1+C])
    dlis = dat[2+C:2+C+D]
    nlis = dat[-1]

    #print clis
    cdict = {}
    for c in clis:
        cdict[c[:2]] = c[2]
    #print cdict
    #print dlis
    #print nlis
    
    w = ""
    for ch in nlis:
        w+=ch

        if len(w) >= 2 and w[-1]+w[-2] in cdict:
            w = w[:-2] + cdict[w[-1]+w[-2]]
        if len(w) >= 2 and w[-2]+w[-1] in cdict:
            w = w[:-2] + cdict[w[-2]+w[-1]]


        for x in dlis:
            if x[0] in w and x[1] in w:
                w = ""

        ##if len(w) >= 2 and w[-2]+w[-1] in dlis:
        ##    w = w[:-2]
        ##if len(w) >= 2 and w[-1]+w[-2] in dlis:
        ##    w = w[:-2]
            
        ##if len(w) >= 3 and w[-3]+w[-1] in dlis:
        ##    w = w[:-3]
        ##if len(w) >= 3 and w[-1]+w[-3] in dlis:
        ##    w = w[:-3]
        #print w
    
    ans = "[" + ", ".join(w) + "]"
    print "Case #%d: %s" % (i+1, ans)
        