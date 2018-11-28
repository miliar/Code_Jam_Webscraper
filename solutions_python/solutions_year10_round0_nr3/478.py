def ROLLER(filename):
    f = open(filename,'r')
    g = open('C-small-attemt0.out','w')
    t = int(f.readline())
    for i in range(0,t):
        rkn = f.readline().split(' ')
        R = int(rkn[0])
        k = int(rkn[1])
        N = int(rkn[2])
        groups = f.readline().split(' ')
        groups = [int(x) for x in groups]
        money = 0
        for ride in range(0,R):
            ppl = 0
            this_ride = []
            done = False
            while len(groups) > 0 and not done:
                if ppl + groups[0] <= k:
                    gp = groups.pop(0)
                    ppl += gp
                    this_ride.append(gp)
                else:
                    done = True
            money += ppl
            groups.extend(this_ride)
        g.write('Case #%s: %s\n' % (i+1,money))

ROLLER('./C-small-attempt0.in')
