def solve(ws,l,cur):
    global res,mincur
    #print ws,cur
    assert len(l)>0
    c = l.pop()
    sets = {}
    foundLetter = False
    for wID,wl in ws:
        word = words[wID]
        sig = []
        for i in range(len(word)):
            if word[i]==c:
                sig.append(i)
                foundLetter = True
        if wl==len(sig):
            #print words[wID],cur,wl,sig,c
            if cur>mincur or (cur==mincur and wID<res):
                mincur = cur
                res = wID
            continue
        tmp = sets.setdefault(tuple(sig),[])
        tmp.append((wID,wl-len(sig)))
    for key,val in sets.iteritems():
        if len(key)==0 and foundLetter:
            solve(val,l,cur+1)
        else:
            solve(val,l,cur)
    l.append(c)
    
fi = open("input.txt")
T = int(fi.readline())
for test in range(T):
    N,M = map(int,fi.readline().split())
    words = []
    for i in range(N):
        words.append(fi.readline().strip())
    lists = []
    for i in range(M):
        lists.append(fi.readline().strip())

    print "Case #"+str(test+1)+":",
    for l in lists:
        mincur = -1
        res = ""
        ws = range(N)
        ls = {}
        for wid in ws:
            tmp = ls.setdefault(len(words[wid]),[])
            tmp.append((wid,len(words[wid])))
        for key,val in ls.iteritems():
            solve(val,list(l[::-1]),0)
        print words[res],
    print ""
