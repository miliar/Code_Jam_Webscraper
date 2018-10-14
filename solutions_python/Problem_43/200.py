#!/usr/bin/env python
"""
usage: python file.py < X-small/large.in
"""

def main():
    for casenum in range(input()):
        numstr = raw_input()
        numlist = [i for i in numstr]
        digcount = len(set(numlist))
        digcount = max(digcount, 2)

        repl = {}
        next_int = 1
        first_sub = False
        for i in range(len(numlist)):
            repcode = repl.get(numlist[i], None)
            if repcode is None:
                if first_sub:
                    first_sub = False
                    repl[numlist[i]] = 0
                    continue
                repl[numlist[i]] = next_int
                next_int += 1
                if i == 0:
                    first_sub = True
        for i in range(len(numlist)):
            repcode = repl.get(numlist[i], None)
            numlist[i] = repcode
        a=''.join([str(i) for i in numlist])

        print 'Case #%d: %d' % (casenum + 1, int(a, digcount))

if __name__ == '__main__':
    try:
        import psyco
        psyco.full()
    except ImportError:
        pass
    main()
