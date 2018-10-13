#!/usr/bin/env python
import sys

class Snapper(object):
    def __init__(self):
        self.state = False

def snap(n, k):
    snappers = []
    for i in range(n):
        snappers.append(Snapper())
    for i in range(k):
        prev_state = snappers[0].state
        snappers[0].state = not snappers[0].state
        for s in range(1, n):
            if not prev_state:
                break
            prev_state = snappers[s].state
            snappers[s].state = not snappers[s].state
    for s in snappers:
        if not s.state:
            return False
    return True

def main(infile):
    f = open(infile)
    t = int(f.readline())
    case = 1
    for l in f.readlines():
        l.strip()
        if not l:
            continue
        n, k = l.split()
        s = snap(int(n), int(k))
        if s:
            state = 'ON'
        else:
            state = 'OFF'
        print 'Case #%d: %s' % (case, state)
        case += 1
    f.close()
    
if __name__ == '__main__':
    main(sys.argv[1])


