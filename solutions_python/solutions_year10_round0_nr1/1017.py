import sys

sys.stdin.readline()

class Snapper(object):
    def __init__(self):
        self.state = 'OFF'
        self.powered = False

    def on_snap(self):
        if not self.powered: return
        if self.state == 'OFF':
            self.state = 'ON'
        elif self.state == 'ON':
            self.state = 'OFF'

    def __str__(self):
        return str((self.powered, self.state))

    def __repr__(self):
        return str(self)

def solve(N, K):
    # one extra snapper is the 'light'
    snappers = [Snapper() for i in range(N+1)]
    snappers[0].powered = True
    for _ in xrange(K):
        [snapper.on_snap() for snapper in snappers[:-1]]
        for i in xrange(N):
            snapper = snappers[i]
            if snapper.powered and snapper.state == 'ON':
                snappers[i+1].powered = True
            else:
                #print 'Switcing off all after ', i+1
                for sn in snappers[i+1:]:
                    sn.powered = False
        #print 'After snap %d: %s'%(_+1, snappers)
#    print 'FINALLY'
#    print snappers
    if snappers[-1].powered:
        return 'ON'
    else:
        return 'OFF'

i = 1
for line in sys.stdin.xreadlines():
    N, K = tuple(map(int, line.split()))
    soln = solve(N, K)
    print 'Case #%d: %s'%(i, soln)
    i += 1
