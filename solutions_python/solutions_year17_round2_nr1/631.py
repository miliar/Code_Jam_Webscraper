def steed(D, N, SP, MS):
    mT = 0.0  # max time
    for i in xrange(N):
        cT = (float(D) - float(SP[i]))/ float(MS[i])
        mT = max(cT, mT)
    return float(D)/mT


t = int(raw_input())

for x in xrange(1, t+1):
    D, N = map(int, raw_input().split(' '))
    SP = []  # starting positions
    MS = []  # maximum speeds
    
    for _ in xrange(N):
        SPi, MSi = map(int, raw_input().split(' '))
        SP.append(SPi)
        MS.append(MSi)
    print 'Case #{}: {}'.format(x, steed(D, N, SP, MS))