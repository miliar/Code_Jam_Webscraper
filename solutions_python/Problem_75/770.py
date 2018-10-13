# Google Code Jam 2011
# Ertug Karamatli
# karamatli.com

import sys

class TestCase(object):
    def __init__(self, case):
        self.case = case
        self.elemlist = []

    def combine(self, combinelist):
        tailpair = self.elemlist[-2:]
        for item in combinelist:
            s = item[0]
            if (s[0] == tailpair[0] and s[1] == tailpair[1]) \
                   or (s[0] == tailpair[1] and s[1] == tailpair[0]):
                self.elemlist.pop()
                self.elemlist.pop()
                self.elemlist.append(item[1])

    def oppose(self, opposelist):
        tail = self.elemlist[-1:][0]
        head = self.elemlist[:-1]
        for item in opposelist:
            if (tail == item[0] and item[1] in head) \
                   or (tail == item[1] and item[0] in head):
                self.elemlist = []
        
    def run(self):
        combinelist, opposelist, invokelist = self.case
        #print combinelist, opposelist, invokelist
        
        for base_elem in invokelist:
            self.elemlist.append(base_elem)
            
            if len(self.elemlist) >= 2:
                self.combine(combinelist)
                self.oppose(opposelist)
            #print self.elemlist

        return self.elemlist

cases = []

f = file(sys.argv[1])
for i, line in enumerate(f):
    if i > 0:
        lst = line.split()

        combine = []
        C = int(lst[0])
        for j in range(1, C+1):
            s = lst[j]
            combine.append((s[:2], s[2]))

        oppose = []
        D = int(lst[C+1])
        for j in range(C+2, C+D+2):
            s = lst[j]
            oppose.append(s)
        
        invoke = lst[C+D+3]
        cases.append((combine, oppose, invoke))

i = 1
for case in cases:
    r = TestCase(case).run()
    print 'Case #%s: %s' % (i, str(r).replace('\'',''))
    i += 1
