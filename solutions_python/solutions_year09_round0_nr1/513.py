#!/usr/bin/python
import re

if __name__ == '__main__':
    fin = open('A-small-attempt0.in', 'r')
    fout = open('A-small-attempt0.out', 'w')
    head = fin.readline()
    head = head.split()
    print head
    L = int(head[0])
    D = int(head[1])
    N = int(head[2])
    dlist = []
    count = 0
    for i in xrange(D):
        line = fin.readline()
        dlist.append(line)
    for i in xrange(N):
        line = fin.readline()
        line = line.replace('(', '[')
        line = line.replace(')', ']')
        line = '^%s$' % line
        count = 0
        for w in dlist:
            if re.match(line, w):
                count += 1
        fout.write('Case #%d: %d\n' % (i+1, count))
