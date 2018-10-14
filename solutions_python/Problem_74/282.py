from collections import deque

f = open('A-large.in', 'r')
cases = int(f.readline())
for case in range(cases):
    line = f.readline()
    l = [s for s in line.split()]
    numB = l[0]
    oq = deque([])
    bq = deque([])
    totq = deque([])
    for i,v in enumerate(l[1:]):
        if v is 'O':
            oq.append(int(l[i+2]))
            totq.append('O'+l[i+2])
        elif v is 'B':
            bq.append(int(l[i+2]))
            totq.append('B'+l[i+2])

    sec = 0
    opos = 1
    bpos = 1

    while (len(totq) > 0):
        nexti = totq[0]
        if nexti[0] == 'O':
            tpass = abs(int(nexti[1:])-opos)+1
            opos=oq[0]            
            if len(bq)>0:
                nextb = bq[0]
                if (nextb > bpos):
                    bpos += min((nextb-bpos),tpass)
                elif (nextb < bpos):
                    bpos -= min((bpos-nextb),tpass)
            sec += tpass              
            oq.popleft()
            totq.popleft()         
        elif nexti[0] == 'B':
            tpass = abs(int(nexti[1:])-bpos)+1
            bpos=bq[0]
            if len(oq)>0:
                nexto = oq[0]
                if (nexto > opos):
                    opos += min((nexto-opos),tpass)
                elif (nexto < opos):
                    opos -= min((opos-nexto),tpass)
            sec += tpass              
            bq.popleft()
            totq.popleft()


    print "Case #%s: %s" % (case+1, sec)
