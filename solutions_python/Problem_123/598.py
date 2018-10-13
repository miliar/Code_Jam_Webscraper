import sys

def consume(armin, mote_sizes):
    if not mote_sizes:
        return 0
    else:
        if armin > mote_sizes[0]:
            return consume(armin + mote_sizes[0], mote_sizes[1:])
        elif 2 * armin - 1 > mote_sizes[0]:
            return 1 + consume(2 * armin - 1, mote_sizes)
        else:
            remove_mote = 1 + consume(armin, mote_sizes[1:])
            if armin > 1:
                try:
                    add_mote = 1 + consume(2 * armin - 1, mote_sizes)
                    return min(add_mote, remove_mote)
                except:
                    pass
            return remove_mote


if __name__ == '__main__':
    cases = int(sys.stdin.readline())
    for case in range(cases):
        armin, motes = [int(i) for i in sys.stdin.readline().split()]
        mote_sizes = [int(i) for i in sys.stdin.readline().split()]
        try:
            print "Case #%d: %d" % (case + 1, consume(armin, sorted(mote_sizes)))
        except Exception, e:
            print e
            print armin, motes, mote_sizes

