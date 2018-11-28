#!/usr/bin/env python

import fileinput, collections, sys, operator, itertools

def autodict():
    return collections.defaultdict(autodict)

def input():
    it = iter(itertools.imap(str.rstrip, fileinput.input()))
    it.next()
    while True:
        yield map(int, it.next().rstrip().split())

def awesome(x):
    y=100

    for num in [2,2,5,5]:
        if x % num == 0 and y % num == 0:
            x /= num
            y /= num

    return y


def main():
    for casenum, (n,pd,pg) in enumerate(input()):
        if (pg == 100 or pg == 0) and pd != pg:
            res = 'Broken'
        elif awesome(pd) <= n:
            res = 'Possible'
        else:
            res = 'Broken'

        # code
        print "Case #%d: %s" % (casenum+1, res)



#for i in xrange(101):
#    print i,awesome(i)
#sys.exit()


main()
