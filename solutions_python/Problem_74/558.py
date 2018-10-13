T = int(raw_input())

for i in range(T):
    D = raw_input().split()
    #print D
    
    op, bp = 1, 1
    ot, bt = 0, 0
    t = 0

    for j in range(int(D[0])):
        ch, npos = D[2*j+1], int(D[2*j+2])
        #print j, ch, npos
        if ch == "O":
            ret = max( abs(npos - op) - (t - ot)+1, 1 )
            ot = t + ret
            op = npos

        if ch == "B":
            ret = max( abs(npos - bp) - (t - bt)+1, 1 )
            bt = t + ret
            bp = npos

        t = t+ret

        #print "val:", ot, bt

    print "Case #%d: %d" % (i+1, t)
