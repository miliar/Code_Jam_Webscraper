#!/usr/bin/env python

import sys

def line():
    return sys.stdin.readline().strip()

def intline():
    return map(int, line().split())

def main(argv):
    t = int(line())
    for caseno in xrange(t):
        row = intline()
        l,t,n,c = row[:4]
        ais = row[4:]
        assert len(ais) == c
        dists = []
        i = 0
        while len(dists) < n:
            dists.append(ais[i % c])
            i += 1
        time2n = [0]
        for d in dists:
            time2n.append(time2n[-1] + 2*d)
        first = None
        for ix,time in enumerate(time2n):
            if time >= t:
                first = ix
                break
        if first is None:
            print "Case #%d: %d" % (caseno + 1, time2n[-1])
            continue
        time2n2 = [x - t for x in list(time2n[first:])]
        diffs = []
        prev = 0
        for x in time2n2:
            diffs.append(x - prev)
            prev = x
        pairs = [(d,ix) for ix,d in enumerate(diffs)]
        pairs.sort()
        pairs.reverse()
        pairsout = []
        for pix in xrange(l):
            if l >= len(pairs):
                break
            d,ix = pairs[pix]
            pairsout.append((d/2, ix))
        pairsout.extend(pairs[l:])
        for d,ix in pairsout:
            diffs[ix] = d
        time = t
        for d in diffs:
            time += d
        print "Case #%d: %d" % (caseno + 1, time)
        
            

if __name__ == "__main__":
    sys.exit(main(sys.argv))
