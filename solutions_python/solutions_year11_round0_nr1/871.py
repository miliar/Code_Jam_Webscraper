import sys#, unicodedata
test = sys.stdin.readlines()
#unicodedata.normalize('NFKD', test[0].decode('utf-8')).encode('ascii','ignore')
ncases = int(test[0].rstrip('\n'))
for i in range(1, ncases+1):
    pbm = test[i].rstrip('\n').split(' ')
    npushs = pbm[0]
    cpO = 1
    cpB = 1
    minsteps = 0
    idleO = 0
    idleB = 0
    for p in range(1, len(pbm), 2):
        goal = int(pbm[p+1])
        if pbm[p] == 'O':
            ns = abs(goal - cpO) 
            if ns > idleO:
                tim = ns - idleO + 1
                idleB += tim
                minsteps += tim
            else:
                minsteps += 1 # + 1 for pushing
                idleB += 1
            cpO = goal
            idleO = 0
        else:
            ns = abs(goal - cpB) 
            if ns > idleB:
                tim = ns - idleB + 1
                idleO += tim
                minsteps += tim
            else:
                minsteps += 1 # + 1 for pushing
                idleO += 1
            cpB = goal
            idleB = 0
    print "Case #"+str(i)+": "+str(minsteps)
