f = open('A-large.in', 'r')
cases = int(f.readline())
for case in range(cases):
    N = int(f.readline())
    pd = {}
    ps = []
    pg = {}

    for playerInd in range(N):
        Ngames = N-1.0
        l = f.readline()
        sm = 0.0
        for i, ch in enumerate(l):
            if playerInd == i: continue
            if ch == "1":
                sm += 1.0
            elif ch == ".":
                Ngames -= 1.0
        pd[playerInd] = sm/Ngames
        ps.append(l)
        pg[playerInd] = Ngames

    print "Case #%s:" % (case+1)

    owpd = {}
    for i in range(N):
        l = ps[i]
        owpL = []
        for j in range(N):
            if i == j or l[j] == ".": continue
            score = pd[j]*pg[j]
            if l[j] == "0":
                score -= 1
            owp = score/(pg[j]-1.0)
            owpL.append(owp)            
        owp = sum(owpL)/pg[i]
        owpd[i] = owp
    
    for i in range(N):
        l = ps[i]
        sm = 0.0
        for j in range(N):
            if i==j or l[j] == ".": continue
            sm += owpd[j]
        oowp = sm/pg[i]

        #print pd[i]
        #print owpd[i]
        #print oowp

        print 0.25*pd[i] + 0.5*owpd[i] + 0.25*oowp
    




