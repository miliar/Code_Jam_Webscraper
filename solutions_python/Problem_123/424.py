def absorb(a, motes):
    while True:
        old = motes[:]
        for m in motes:
            if m < a:
                a += m
                motes.remove(m)
        if motes == old:
            return a, motes


def solve_case(me, other_motes):
    if me == 1:
        return len(other_motes)
    motes = other_motes[:]
    ops = 0
    a = me 
    while True:
        motes.sort()
        me, motes = absorb(me, motes)
        if not motes:
            break
        # Add
        if 2 * me - 1 > motes[0]:
            ops += 1
            motes.append(me - 1)
        # Remove
        else:
            ops += 1
            k = motes.pop()
    ops2 = 0
    motes = other_motes[:]
    while True:
        motes.sort()
        a, motes = absorb(a, motes)
        if not motes:
            break
        ops2 += 1
        motes.append(a - 1)
    return min(ops, ops2) or ops


if __name__ == '__main__':
    import sys
    r = sys.stdin.readline
    t = int(r())
    for i in xrange(t):
        me = int(r().split()[0])
        motes = map(int, r().split())
        print 'Case #{0}: {1}'.format(i + 1, solve_case(me, motes))
