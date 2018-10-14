"""Usage:
    X.py < X.in > X.out
"""
from numpy import array, nan, nanargmax, zeros, isnan
def setup(infile):
    #C = {}
    return locals()

def reader(testcase, infile, **ignore):
    #N = int(infile.next())
    #P = map(int, infile.next().split())
    #I = map(int, infile.next().split())
    #T = infile.next().split()
    #S = [infile.next().strip() for i in range(N)]
    return locals()

def solver(infile, testcase, N=None, P=None, I=None, T=None, S=None, C=None, **ignore):
    from numpy import array, delete, argmin, max

    d = {'X':1,'O':-1,'.':nan,'T':0}
    n_lines = 4
    
    results = zeros(10)
    for l in range(n_lines):
        row = array(map(lambda c: d[c], infile.next().strip()))
        results[0:4] += row[0:4]
        results[4] += row[l]
        results[5] += row[-l-1]
        results[6+l] = sum(row)
    
    ind = nanargmax(abs(results))
    if ind is nan:
        res = 'Game has not completed'
    elif results[ind] >=3:
        res = 'X won'
    elif results[ind] <= -3:
        res = 'O won'
    else:
        if isnan(results.sum()):
            res = 'Game has not completed'
        else:
            res = 'Draw'
    infile.next()

    return 'Case #%s: %s\n' % (testcase, res)

if __name__ == '__main__':
    import sys
    T = int(sys.stdin.next())
    common = setup(sys.stdin)
    for t in xrange(1, T+1):
        sys.stdout.write(solver(**reader(t, **common)))
