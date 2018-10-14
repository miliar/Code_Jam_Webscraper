from sys import stdout
from collections import defaultdict

ifile = open('../input/C-small-attempt0.in', 'r')
#ifile = open('../input/C.x.in', 'r')
ofile = open('../output/C-small-attempt0.out', 'w')
#ofile = stdout

cases = int(ifile.readline())

def find(n, notes):
    for x in notes:
        if x % n != 0 and n % x != 0:
            return False
    return True

for case in xrange(cases):
    n, l, h = map(int, ifile.readline().split())
    notes = map(int, ifile.readline().split())
    note = None
    for x in xrange(l, h+1):
        if find(x, notes):
            note = x
            break
    if note:
        ofile.write('Case #%d: %d\n' % (case+1, note))
    else:
        ofile.write('Case #%d: NO\n' % (case+1))
    
        
    
