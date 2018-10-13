f = open("inb.txt","r")
out = open("outb.txt","w")
cases = int(f.readline())
for case in xrange(1,cases+1):
    line = f.readline().split()
    k = int(line[0])
    transfers = []
    trans = []
    for i in xrange(k):
        t = []
        for ch in line[i+1]:
            t.append(ch)
            if not ch in transfers:
                transfers.append(ch)
        trans.append(t)
    rems = []
    removers = []
    n = int(line[k+1])
    for i in xrange(n):
        t = []
        for ch in line[i+k+2]:
            t.append(ch)
            if not ch in removers:
                removers.append(ch)
        rems.append(t)
    lens = int(line[n+k+2])
    analyse = line[n+k+3]
    res = []
    inp = []
    for ch in analyse:
        inp.append(ch)
    for ch in inp:
        tr = False
        if len(res)>0:
            if ch in transfers:
                for tran in trans:
                    if ch in tran:
                        if tran[0]==ch:
                            if res[-1]==tran[1]:
                                res[-1]=tran[2]
                                tr = True
                                break
                        if tran[1]==ch:
                            if res[-1]==tran[0]:
                                res[-1]=tran[2]
                                tr = True
                                break
            if not tr:
                if ch in removers:
                    for rem in rems:
                        if rem[0]==ch:
                            if rem[1] in res:
                                res = []
                                tr = True
                                break
                        elif rem[1]==ch:
                            if rem[0] in res:
                                res=[]
                                tr = True
                                break
        if not tr:res.append(ch)
    out.write("Case #%d: [" % (case) )
    if len(res)>0:
        for i in res[:-1]:out.write("%c, "%i)
        out.write("%c"%res[-1])
    out.write("]\n")