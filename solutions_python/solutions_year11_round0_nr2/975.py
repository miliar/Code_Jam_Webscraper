#!/usr/bin/python

def process(case, credit, itemcount, items):
    pass

ifh = open('B-large-0.in', 'rb')
ofh = open('B-large-0.out', 'wb')

testcases = int(ifh.readline())

debug = 0

def dp(s):
    if debug:
        print s

def addcombiner(cd, b1, b2, nb):
    cd[b1 + b2] = nb
    cd[b2 + b1] = nb

def addopposer(od, o1, o2):
    od.append(o1 + o2)
    od.append(o2 + o1)

def combine(comb, test):
    if test in comb:
        return comb[test]

def checkoppose(elementlist, opposers):
    ne = elementlist[-1]
    oldelements = elementlist[:-1]
    for oe in oldelements:
        if (oe + ne) in opposers:
            dp("   found %s opposer, clearing list" % (oe+ne,))
            elementlist = []
            break
    return elementlist

def process(caseno, comb, oppo, invokes):
    dp("%d comb: %s oppo: %s invokes: %s" % (caseno, comb, oppo, invokes))
    el = []
    for i in invokes:
        dp("  element list : %s" % (el,))
        dp("  Invoking %s" % (i,))
        el.append(i)
        if len(el) > 1:
            testelements = el[-2:]
            nb = combine(comb, ''.join(testelements))
            if nb:
                el.pop()
                el.pop()
                el.append(nb)
                dp("  Combined elements %s into %s" % (''.join(testelements), nb))
            else:
                el = checkoppose(el, oppo)
    return "[%s]" % ', '.join(el)

for case in range(1, int(testcases) + 1):
    rec = ifh.readline().split()
    combinecount = int(rec.pop(0)) # strip off first field
    combiners = {}
    for i in range(0, combinecount):
        c = list(rec.pop(0))
        addcombiner(combiners, *c)
    opposercount = int(rec.pop(0))
    opposers = []
    for i in range(0, opposercount):
        o = list(rec.pop(0))
        addopposer(opposers, *o)
    invokecount = int(rec.pop(0))
    invokelist = list(rec.pop(0))
    ofh.write('Case #%d: %s\n' % (case, process(case, combiners, opposers, invokelist)))

ifh.close()
ofh.close()
