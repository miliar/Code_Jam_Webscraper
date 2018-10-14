def get_result(r,d,f):
    base = ['Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F']
    rr = [] # real queue
    bq = [] # base queue
    r_a = {}
    for e in r:
        r_a[e[0]+e[1]] = e[2]
        r_a[e[1]+e[0]] = e[2]
    d_a = {}
    for e in d:
        if e[0] in d_a:
            d_a[e[0]].append(e[1])
        else:
            d_a[e[0]]=[e[1]]
        if e[1] in d_a:
            d_a[e[1]].append(e[0])
        else:
            d_a[e[1]]=[e[0]]
    c = 1
    if len(f)>0:
        rr = [f[0]]
#    print r_a,d_a
    while(c<len(f)):
        if len(rr)>0 and r_a.has_key(f[c]+rr[len(rr)-1]):
#            print f[c],c,"1"
            j = rr.pop()
            rr.append(r_a[f[c]+j])
        elif len(rr)>0 and d_a.has_key(f[c]):
#            print f[c],c,"2"
            o = True
            for k in d_a[f[c]]:
                if k in rr:
                    rr = []
                    o = False
            if o:
                rr.append(f[c])
        else:
#            print f[c],c,"3"
            rr.append(f[c])
#            print rr
        c = c+1
    ret = "["
    for r in rr:
        ret = ret + r +", "
    ret = ret.strip(" ").strip(",")
    ret = ret + "]"
    return ret
f = open("B-large.in","r")
c = 0 
for l in f:
    if c==0:
        c = c + 1
        continue
    s = l.split(" ")
    r_arr = []
    d_arr = []
    r_c = int(s[0])
    s_c = 1
    r_remain = True
    while(s_c<(len(s)-2)):
        if r_c>0:
            r_arr.append(s[s_c])
            r_c = r_c - 1 
        elif r_c==0 and r_remain:
            d_c = int(s[s_c])
            r_remain = False
        elif d_c>0:
            d_arr.append(s[s_c])
            d_c = d_c - 1 
        s_c = s_c + 1
    print "Case #%d: %s" %(c,get_result(r_arr,d_arr,s[len(s)-1].strip("\n")))
    c = c + 1 
f.close()
