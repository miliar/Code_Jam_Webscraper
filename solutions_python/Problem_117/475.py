"""Usage:
    X.py < X.in > X.out
"""

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

    rowN, colN = map(int,infile.next().split())
    lawn = []
    for l in range(rowN):
        lawn.append(map(int,infile.next().split()))
    lawn = array(lawn)
    res = 'YES'
    while lawn.size > 1:
        indMin = argmin(lawn.ravel())
        colMin = indMin % lawn.shape[1]
        rowMin = indMin / lawn.shape[1]
        if lawn[rowMin, colMin] == max(lawn[rowMin, :]):
            lawn = delete(lawn, rowMin, 0)
        elif lawn[rowMin, colMin] == max(lawn[:, colMin]):
            lawn = delete(lawn, colMin, 1)
        else:
            res = 'NO'
            break
   
    return 'Case #%s: %s\n' % (testcase, res)

if __name__ == '__main__':
    import sys
    T = int(sys.stdin.next())
    common = setup(sys.stdin)
    for t in xrange(1, T+1):
        sys.stdout.write(solver(**reader(t, **common)))
