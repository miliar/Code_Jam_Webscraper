import sys, itertools, pdb

def main():
    filePrefix = 'B-large'
    fin = open(filePrefix + '.in', 'r')
    fout = open(filePrefix + '.out', 'w')
    T = int(fin.readline().strip())
    for t in xrange(T):
        H, W = [int(x) for x in (fin.readline().strip().split())]
        elmap = []
        for h in xrange(H):
            elmap.append([int(x) for x in fin.readline().strip().split()])
        #print_map(elmap)

        sheds = dict([(x, x[0] * W + x[1])
                      for x in itertools.product(xrange(H), xrange(W))])
        equivalencies = [set([x[0] * W + x[1]])
                         for x in itertools.product(xrange(H), xrange(W))]

        for h in xrange(H):
            for w in xrange(W):
                outlet = get_outlet(elmap, h, w, H, W)
                if outlet:
                    oldShed = sheds[(h, w)]
                    outShed = sheds[outlet]
                    merge_sheds(equivalencies, oldShed, outShed)
        equivalencies.sort(key = lambda x: min(x))

        shedLabels = {}
        nextShedLabelNum = 97
        for equivSet in equivalencies:
            shedLabel = chr(nextShedLabelNum)
            nextShedLabelNum += 1
            for shedNum in equivSet:
                shedLabels[shedNum] = shedLabel

        fout.write("Case #%d:\n" % (t+1))
        for h in xrange(H):
            for w in xrange(W):
                fout.write('%s ' % shedLabels[sheds[(h, w)]])
            fout.write("\n")

    fin.close()
    fout.close()


def merge_sheds(equivs, s1, s2):
    e1, e2 = None, None
    for e in equivs:
        if s1 in e: e1 = e
        if s2 in e: e2 = e
        if e1 != None and e2 != None: break
    if e1 != e2:
        e1.update(e2)
        equivs.remove(e2)


def get_outlet(elmap, h, w, H, W):
    el = elmap[h][w]
    minEl, outlet = el, None
    for (y, x) in ((h-1, w), (h, w-1), (h, w+1), (h+1, w)):
        if (y >= 0) and (y < H) and (x >= 0) and (x < W) and \
                elmap[y][x] < minEl:
            minEl, outlet = elmap[y][x], (y, x)
    return outlet


def print_map(elmap):
    for r in elmap:
        for c in r:
            print (" %d" % c),
        print ""
    print ""




