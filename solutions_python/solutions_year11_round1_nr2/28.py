def play(g, w, ws):
    pos = {}
    for ww in ws:
        pos[ww] = len(ww) == len(w)

    posw = [k for k, v in pos.iteritems() if v]
    if len(posw) == 1:
        return 0

    score = 0
    for ch in g:
        go = any(ch in ww for ww in posw)

        if go:
            if ch not in w:
                score += 1
                for ww in posw:
                    if ch in ww:
                        pos[ww] = False
            else:
                idxs = [i for i, c in enumerate(w) if c == ch]

                for ww in posw:
                    idxs2 = [i for i, c in enumerate(ww) if c == ch]
                    if idxs2 != idxs:
                        pos[ww] = False

        posw = [k for k, v in pos.iteritems() if v]
        if len(posw) == 1: return score

    assert False

if __name__ == '__main__':
    T = int(raw_input())
    for caseno in xrange(T):
        N, M = [int(s) for s in raw_input().split()]
        ws = []
        for _ in xrange(N):
            ws += [raw_input()]

        gs = []
        for _ in xrange(M):
            gs += [raw_input()]

        res = []
        for g in gs:
            best, bestw = None, None
            for w in ws:
                score = play(g, w, ws)

                if best is None or score > best:
                    best = score
                    bestw = w
            res += [bestw]

        print 'Case #%d: %s' % (caseno + 1, ' '.join(res))
