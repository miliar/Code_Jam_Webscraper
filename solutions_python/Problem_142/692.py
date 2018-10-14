ri = lambda : raw_input().strip()
rim = lambda tp, deli: map(tp, ri().split(deli))

num = int(ri())


    
    
for i in xrange(0, num):
    n = int(ri())
    result = 0
    data = []
    for j in xrange(n):
        data.append(ri())

    data = sorted(data)
    sx = []
    st = []
    
    tt = [""]
    for ch in data[0]:
        if tt[-1] != ch:
            tt.append(ch) 
        
    da = []
    for s in data:
        va = {}
        tmp2 = [""]
        ct = 0
        zv = []
        for ch in s:
        
            if ch not in va:
                va[ch] = 1
            else:
                va[ch] += 1
                
            if tmp2[-1] != ch:
                tmp2.append(ch)
                zv.append(ct)
                ct = 1
                
            else:
                ct += 1
                
        if tmp2 != tt:
            result = "Fegla Won"
            
        zv.append(ct)        
        sx.append(va)
        da.append(zv)
        

    print "Case #{}:".format(i+1),
    
    if result == "Fegla Won":
        pass
        
    else:
        for x in xrange(len(da[0])):
            tmp = []
            for d in da:
                tmp.append(d[x])

            result += max(tmp) - min(tmp)    
                
    if result == 0:
        if data[0] != data[1]:
            result = "Fegla Won"

    print result
    
    
    
    
    