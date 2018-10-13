#!/usr/bin/env python

import sys

def line():
    return sys.stdin.readline().strip()

def intline():
    return map(int, line().split())

def main(argv):
    t = int(line())
    for caseno in xrange(t):
        r,c = intline()
        rows = []
        for ixr in xrange(r):
            rows.append(line())
        out = []
        if not rows:
            print "Case #%d:" % (caseno + 1)
            continue
        out.append([])
        right = False
        for c in rows[0]:
            if c == '#':
                out[0].append(1 if right else 0)
                right = not right
            else:
                out[0].append('.')
        if right:
            print "Case #%d:\nImpossible" % (caseno + 1)
            continue
        success = True
        for ix,r in enumerate(rows[1:]):
            prev = out[ix]
            right = False
            rowout = []
            for ixc,c in enumerate(r):
                if c == '#':
                    if prev[ixc] == 0:
                        if right:
                            success = False
                            break
                        rowout.append(2)
                        right = not right
                    elif prev[ixc] == 1:
                        if not right:
                            success = False
                            break
                        rowout.append(3)
                        right = not right
                    else:
                        rowout.append(1 if right else 0)
                        right = not right
                else:
                    if prev[ixc] == 0 or prev[ixc] == 1:
                        success = False
                        break
                    rowout.append('.')
            if right:
                success = False
            if not success:
                break
            out.append(rowout)
            
        if 0 in out[-1] or 1 in out[-1]:
            success = False
        print "Case #%d:" % (caseno + 1)
        if not success:
            print "Impossible"
        else:
            tojoin = []
            for r in out:
                rout = []
                for c in r:
                    if c == '.':
                        rout.append('.')
                    else:
                        rout.append('/\\\\/'[c])
                tojoin.append("".join(rout))
            print "\n".join(tojoin)
                        

if __name__ == "__main__":
    sys.exit(main(sys.argv))
