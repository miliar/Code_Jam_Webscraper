def go(oriset, data):
    res=0
    for d in data:
        #print d
        x=0
        while (True):
            
            if d in oriset:
                res+=x
                break
            else:
                oriset.add(d)
                d=d[:d.rindex("/")]
                x+=1
    return res

cn=input()
for c in xrange(cn):
    oriset=set()
    oriset.add("/")
    oriset.add("")
    orin, mkn=[int(k) for k in raw_input().split()]
    data=[]
    for i in xrange(orin):
        temp=raw_input()
        oriset.add(temp)
    for i in xrange(mkn):
        data.append(raw_input())
    data.sort()
    res=go(oriset, data)

    print "Case #%d: %d" %(c+1, res)
