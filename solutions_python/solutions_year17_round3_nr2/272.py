J, C = range(2)


def sol(cis, jis):
    print
    stuff = sorted(
        [(ji[0], ji[1], J) for ji in jis] +
        [(ci[0], ci[1], C) for ci in cis])
    print "stuff: %s" % (stuff,)
 
    blocks = []
    curr = stuff[0][2]
    low = stuff[0][0]
    for i, (st, fi, who) in enumerate(stuff):
        if who != curr:
            high = stuff[i - 1][1]
            blocks.append((low, high, curr))
            
            curr = who
            low = st

    high = stuff[-1][1]
    blocks.append((low, high, curr))
    print "blocks: %s" % (blocks,)

    if len(blocks) == 1:
        if blocks[0][1] - blocks[0][0] <= 720:
            return 2
        ret = 0
    else:
        ret = len(blocks) - 1 if blocks[0][-1] == blocks[-1][-1] else len(blocks)
    print "ret before: %s" % (ret,)

    j, c = 0, 0
    for low, high, curr in blocks:
        if curr == C:
            c += high - low
        else:
            j += high - low

    if max(j, c) <= 720:
        return ret
    print "c: %s" % (c,)
    print "j: %s" % (j,)

    ls = len(stuff)
    if j > 720:
        dead_times = []
        need = j - 720 if c != 0 else 720
        print "need: %s" % (need,)

        for i in xrange(ls - 1):
            if stuff[i][-1] == J and stuff[i + 1][-1] == J:
                dead_times.append(stuff[i + 1][0] - stuff[i][1])
        if stuff[-1][-1] == J and stuff[0][-1] == J:
            dead_times.append(stuff[0][0] + 1440 - stuff[-1][1])
        
        dead_times = sorted(dead_times, reverse=True)
        print "dead_times: %s" % (dead_times,)
        for el in dead_times:
            if el >= need:
                ret += 2
                break
            else:
                need -= el
                ret += 2
    else:
        dead_times = []
        need = c - 720 if j != 0 else 720
        print "need: %s" % (need,)
        
        for i in xrange(ls - 1):
            if stuff[i][-1] == C and stuff[i + 1][-1] == C:
                dead_times.append(stuff[i + 1][0] - stuff[i][1])
        if stuff[-1][-1] == C and stuff[0][-1] == C:
            dead_times.append(stuff[0][0] + 1440 - stuff[-1][1])

        dead_times = sorted(dead_times, reverse=True)
        print "dead_times: %s" % (dead_times,)
        for el in dead_times:
            if el >= need:
                ret += 2
                break
            else:
                need -= el
                ret += 2

    return ret


def show(i, val):
    print "Case #%s: %s" % (i, val)


if __name__ == "__main__":
    T = int(raw_input().strip())

    for i in xrange(1, T + 1):
        ac, aj = map(int, raw_input().strip().split())
        cis, jis = [], []
        for _ in xrange(ac):
            st, fi = map(int, raw_input().strip().split())
            cis.append((st, fi))
        for _ in xrange(aj):
            st, fi = map(int, raw_input().strip().split())
            jis.append((st, fi))
        show(i, sol(cis, jis))

