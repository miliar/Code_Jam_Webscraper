import pdb
def solve_case(ln):
    ln = ln.strip().split(' ')
    MX = int(ln[0])
    A = [int(x) for x in list(ln[1])]
    exists = 0
    extra = 0
    for needed, current in enumerate(A):
        if current>0:
            if needed > exists:
                extra += needed - exists
                exists = needed
            exists += current
    return extra


with open('A-large.in') as fin, \
open('A-large.out', 'w') as fout:
    case = 0
    NumCases = int(fin.next())
    for case in xrange(1, NumCases+1):
        line = fin.next()
        fout.write("Case #%d: " % case + str(solve_case(line)) + '\n')
        print line

