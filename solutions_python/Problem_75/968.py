#!/usr/bin/python2
import sys

class ElementList:
    def __init__(self):
        self._elems = []

    def __str__(self):
        return str(self._elems).replace('\'', '')

    def add(self, e):
        self._elems.append(e)

    def length(self):
        return len(self._elems)

    def combine(self, triplet):
        if len(self._elems) < 2:
            return

        candidate = set(self._elems[-2:])

        if set(triplet[0:2]) == candidate:
            self._elems = self._elems[:-2] + list(triplet[2])

    def opposed(self, pair):
        #print set(pair)
        #print set(self._elems)
        if self.length() >= 2 and set(pair).issubset(set(self._elems)):
            self._elems = []

def solve(num, data):
    #print '------ Case #%d ------' % num

    offset = 0
    num_combines = int(data[offset])
    offset += 1

    combines = data[offset:offset+num_combines]
    offset += num_combines

    num_opposed = int(data[offset])
    offset += 1
    opposed = data[offset:offset+num_opposed]
    offset += num_opposed

    num_elements = int(data[offset])
    offset += 1

    elements = ElementList()
    #print 'Pre #%d: %s' % (num, list(data[offset]))

    for e in list(data[offset]):
        elements.add(e)
        #print elements
        map(elements.combine, combines)
        map(elements.opposed, opposed)
        #print elements

    print 'Case #%d: %s' % (num, elements)
    #print 'Combines:', combines
    #print 'Opposed:', opposed
    #print 'Elements:', elements

if len(sys.argv) < 2:
    print 'Usage: %s <input file>' % sys.argv[0]
    sys.exit(1)

fp = open(sys.argv[1])
cases = int(fp.readline())

i = 1
for line in fp:
    solve(i, line.split())
    i += 1
