def parse_result(t):
    p1 = 1 # O
    p2 = 1 # B
    r1 = 0 # reserve moves for O
    r2 = 0 # reserve moves for B
    r = 0
    t_l = len(t)/2
    for j in range(0,t_l):
        pos = j*2
        n_p = int(t[pos+1])
        if(t[pos]=="O"):
            m = abs(n_p-p1)+1
            if m<=r1:
                r1 = 0
                m = 1
            else:
                m = m - r1
                r1 = 0
            r = r + m
            r2 = r2 + m
            p1 = n_p
#            print r1,r2,r
        if(t[pos]=="B"):
            m = abs(n_p-p2)+1
            if m<=r2:
                r2 = 0
                m = 1
            else:
                m = m - r2
                r2 = 0
            r = r + m
            r1 = r1 + m
            p2 = n_p
#            print r1,r2,r
    return r

f = open("A-large.in","r")
c = 0 
for l in f:
    if c==0:
        c = c + 1
        continue
    t = l.strip("\n").split(" ")
    print "Case #%d: %d" % (c,parse_result(t[1:]),)
    c = c + 1
f.close()
