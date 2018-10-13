#!/usr/bin/env python

from collections import defaultdict

def cremove(c, word):
    return str(x for x in word if x != c)

def cidx(c, word):
    return {i for (i,x) in enumerate(word) if x == c}

#def match(word, c, idxl):
    #    return all(word[i] == c for i in idxl)

def match(word, target, gidxs, valid_chars):
    for i, c in enumerate(word):
        if i in gidxs:
            if c != target[i]: return False
        else:
            if c not in valid_chars: return False

    return True

def should(c, wlist, gidxs, valid_chars):
    for (word,prio) in wlist:
        has_c = False
        consistent = True
        for idx, cx in enumerate(word):
            if idx not in gidxs:
                if cx == c:
                    has_c = True
                elif cx not in valid_chars:
                    consistent = False
                    break
        if has_c and consistent:
            return True
    return False

def solve(words, llist):
    best = (12019, 119083801309810, 'ZZZZZZZZZZZZZZZZZZZZZZZZZ')

    def sim(word_, wlist):
        wlist = wlist[:]
        score = 0
        word = word_
        gidxs = set()
        if len(wlist) == 1:
            return score, word_
        for lidx, c in enumerate(llist):
            valid_chars = set(llist[lidx:])
            if not should(c, wlist, gidxs, valid_chars):
                continue
            idxs = cidx(c, word)
            gidxs = gidxs | idxs
            if not idxs:
                score -= 1
            wlist = [x for x in wlist if match(x[0], word_, gidxs, valid_chars)]
            if len(wlist) <= 1:
                break

        return score, word_



    for wsize in words:
        for word, prio in words[wsize]:
            score, word_ = sim(word, words[wsize])
            best = min(best, (score, prio, word))

    return best[2]



if __name__ == '__main__':
    import fileinput

    inp = fileinput.input()

    t = int(inp.readline())

    for i in xrange(1, t+1):
        n, m = map(int, inp.readline().split())
        lwords = [inp.readline().strip() for x in xrange(n)]
        lists = [inp.readline().strip() for x in xrange(m)]

        words = defaultdict(list)
        for idx,word in enumerate(lwords):
            words[len(word)].append((word, idx))

        print 'Case #%d:' % i,

        for llist in lists:
            best = solve(words, llist)
            print '%s' % best,

        print
