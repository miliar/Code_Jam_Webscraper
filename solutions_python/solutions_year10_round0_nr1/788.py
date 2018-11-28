import sys

def debug(s):
    return
    print s

class Chain(object):
    def __init__(self, length):
        self.snappers = [False] * length


    def snap(self):
        for i in range(len(self.snappers)):
            self.snappers[i] = not self.snappers[i]
            if self.snappers[i]:
                break

    def on(self):
        return sum(self.snappers) == len(self.snappers)


def solve(snappers, snaps):
    c = Chain(snappers)
    for j in range(snaps):
        c.snap()
        debug('state: ' + ' '.join(['01'[s] for s in c.snappers][::-1]))
    return c.on()


def fastsolve(snappers, snaps):
    period = (1 << snappers)
    debug('period %d' % (period,))
    debug('snaps %% period %d' % (snaps % period,))
    return (snaps % period) == (period - 1)


def main():
    lines = int(sys.stdin.readline())
    for i in range(lines):
        snappers, snaps = map(int, sys.stdin.readline().split())
        # a = solve(snappers, snaps)
        # b = fastsolve(snappers, snaps)
        # assert a == b, "%r != %r" % (a, b)
        print 'Case #%d:' % (i + 1,),        
        if fastsolve(snappers, snaps):
            print 'ON'
        else:
            print 'OFF'
        


if __name__ == '__main__':
    main()
