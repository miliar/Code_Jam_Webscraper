# Google Code Jam 2011
# Ertug Karamatli
# karamatli.com

import sys
from collections import deque


class TestCase(object):
    def __init__(self, case):
        self.case = case

    def patrick_add(self, lst):
        def add_two(a, b):
            res = []
            a = bin(int(a))[2:]
            b = bin(int(b))[2:]
            la = len(a)
            lb = len(b)
            for i in range(max(la, lb)):
                if la > i and lb > i:
                    s = int(a[la-i-1]) + int(b[lb-i-1])
                elif la > i:
                    s = int(a[la-i-1])
                elif lb > i:
                    s = int(b[lb-i-1])
                
                if s == 2: s = 0
                res.append(s)
            res.reverse()
            res2 = ''
            for bit in res:
                res2 += str(bit)
            return int(res2, 2)
        
        accum = lst[0]
        for item in lst[1:]:
            accum = add_two(accum, item)
        return accum

        #print self.patrick_add([5,4])
        #print self.patrick_add([7,9])
        #print self.patrick_add([50,10])

    def run(self):
        sean_max = -1
        casedeque = deque(self.case)
        for x in range(len(casedeque)):
            case = list(casedeque)
            for i in range(1, len(case)):
                pile1 = case[:i]
                pile1val = int(self.patrick_add(pile1))

                pile2 = case[i:]
                pile2val = int(self.patrick_add(pile2))

                #print pile1, pile2

                if pile1val == pile2val:
                    s1 = sum([int(j) for j in pile1])
                    if s1 > sean_max: sean_max = s1
                    s2 = sum([int(j) for j in pile2])
                    if s2 > sean_max: sean_max = s2

                #print pile1, pile2
                #print pile1val, pile2val
                #print sean_max
                #print
            casedeque.rotate(1)
        
        if sean_max == -1:
            return 'NO'
        return sean_max

cases = []

f = file(sys.argv[1])
for i, line in enumerate(f):
    if i > 0 and i % 2 == 0:
        lst = line.split()
        cases.append(lst)

i = 1
for case in cases:
    r = TestCase(case).run()
    print 'Case #%s: %s' % (i, r)
    i += 1
