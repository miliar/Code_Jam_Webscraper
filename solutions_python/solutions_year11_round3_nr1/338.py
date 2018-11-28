# Google Code Jam 2011
# Ertug Karamatli
# karamatli.com

import sys


class TestCase(object):
    def __init__(self, case):
        self.case = case

    def draw(self, case):
        buf = ''
        lc = len(case)
        i = 0
        for s1 in case:
            for s2 in s1:
                buf += s2
            if lc != i+1: buf += '\n'
            i += 1
        return buf

    def is_impossible(self, case):
        for s1 in case:
            for s2 in s1:
                if s2 == '#':
                    return True
        return False
    
    def run(self):
        #print self.draw(case)
        w = len(case)
        h = len(case[0])
        for i in range(w-1):
            for j in range(h-1):
                if case[i][j] == '#' and case[i+1][j] == '#' and case[i][j+1] == '#' and case[i+1][j+1] == '#':
                    case[i][j] = '/'
                    case[i+1][j] = '\\'
                    case[i][j+1] = '\\'
                    case[i+1][j+1] = '/'

        if self.is_impossible(case):
            return 'Impossible'
        else:
            return self.draw(case)

cases = []

f = file(sys.argv[1])
j = 0
case = []
for i, line in enumerate(f):
    if i > 0:
        if j > 0:
            case.append(list(line.strip()))
            j -= 1
        else:
            if len(case) > 0: cases.append(case)
            case = []
            lst = line.split()
            #print lst
            j = int(lst[0])

cases.append(case)

i = 1
for case in cases:
    r = TestCase(case).run()
    print 'Case #%s:\n%s' % (i, r)
    i += 1
    #if i > 1: break
