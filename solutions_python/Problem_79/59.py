#!/usr/bin/env python

import sys

def main(argv):
    t = int(sys.stdin.readline())
    for caseno in xrange(t):
        n,m = map(int, sys.stdin.readline().strip().split())
        grid = [[set() for _ in xrange(26)] for _ in xrange(10)]
        dorig = []
        for _ in xrange(n):
            word = sys.stdin.readline().strip()
            for ix,c in enumerate(word):
                grid[ix][ord(c) - ord('a')].add(word)
            dorig.append(word)
            
        ls = []
        for _ in xrange(m):
            ls.append(sys.stdin.readline().strip())
        bestwords = []
        all_letters = map(chr, xrange(ord('a'), ord('z') + 1))
        for l in ls:
            bestscore = -1
            bestword = None
            for w in dorig:
                sortw = set(w)
                filt = lambda itr: set([e for e in itr if len(e) == len(w)])
                d = filt(dorig)
                score = 0
                seen = []
                for c in l:
                    if len(d) <= 1:
                        break
                    seen.append(c)
                    if set(seen).intersection(sortw) == sortw:
                        break
                    letters = set()
                    for wprime in d:
                        letters = letters.union(wprime)
                        if len(letters) >= 26:
                            break
                    #print letters, w, c, d
                    if c in letters and c not in w:
                        #print "score on", c, w
                        score += 1
                    for ix,cprime in enumerate(w):
                        s = grid[ix][ord(c) - ord('a')]
                        if cprime == c:
                            d = d.intersection(s)
                        else:
                            d = d.difference(s)
                        if len(d) <= 1:
                            break
                        
                #print w,score,l
                if score > bestscore:
                    bestscore = score
                    bestword = w
            bestwords.append(bestword)
        print "Case #%d: %s" % (caseno + 1, " ".join(bestwords))
        #if caseno == 1:
        #    break

if __name__ == "__main__":
    sys.exit(main(sys.argv))
