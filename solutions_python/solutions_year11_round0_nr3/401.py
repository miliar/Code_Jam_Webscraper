#!/usr/bin/env python
import operator

def main(argv):
    # Parsing our file
    assert(len(argv) == 2)
    fname = argv[1]
    lines = None
    with open(fname) as fd:
        lines = fd.readlines()
    if not lines:
        return
    lines = lines[2::2]
    lines = [map(int, line.split()) for line in lines]
    # playing with XOR
    for testid, test in enumerate(lines, start=1):
        res = 0
        for val in test:
            res ^= val
        if res:
            print 'Case #%d: NO' % testid
            continue
        pilevalue = sum(test) - min(test)
        # Poor Patrick...
        print 'Case #%d: %d' % (testid, pilevalue)

if __name__ == "__main__":
    import sys
    main(sys.argv)

