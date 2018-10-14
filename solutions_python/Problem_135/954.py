

import sys

def readline(index, f):
    for i in xrange(4):
        line = f.readline()
        if index == i:
            s = set(map(int, line.split()))
    return s

if __name__=='__main__':
    f = sys.stdin
    T = int(f.readline())
    for t in xrange(T):
        first = int(f.readline()) - 1
        s1 = readline(first, f)
        second = int(f.readline()) - 1
        s2 = readline(second, f)
        rez = s1 & s2
        if len(rez) == 0:
            ret = 'Volunteer cheated!'
        elif len(rez) == 1:
            ret = rez.pop()
        else:
            ret = 'Bad magician!'
        print 'Case #%s: %s' % (t+1, ret)
