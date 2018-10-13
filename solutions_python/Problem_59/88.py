#!/usr/bin/python

SIZE = 'large'
PROBLEM = 'A'
DATASET = PROBLEM + '-' + SIZE
IFILE = DATASET + '.in'
OFILE = DATASET + '.out'

def get_parents(d):
    parts = d.split('/')
    res = ''
    for p in parts[1:-1]:
        res += '/' + p
        yield res

def solve(present, new):
    present_set = set(present)
    for each in present:
        for parent in get_parents(each):
            present_set.add(parent)
    orig = set(present_set)
    for each in new:
        for parent in get_parents(each):
            present_set.add(parent)
        present_set.add(each)
    return len(present_set) - len(orig)

ifile = open(IFILE, 'r')
ofile = open(OFILE, 'w')
T = int(ifile.readline())
for i in xrange(T):
    line = ifile.readline().strip().split(' ')
    N = int(line[0])
    M = int(line[1])
    present = [ifile.readline().strip() for j in xrange(N)]
    new = [ifile.readline().strip() for j in xrange(M)]
    ofile.write('Case #%s: %s\n' % (i+1,str(solve(present, new))))
ifile.close()
ofile.close()
