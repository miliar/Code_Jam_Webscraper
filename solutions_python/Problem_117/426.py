import os

def column(mat, n):
    return [row[n] for row in mat]

def columns(mat):
    return (column(mat, n) for n in xrange(len(mat[0]))) if mat else ()

def rows(mat):
    return (list(m) for m in mat)

def mkmat(val, m, n):
    return [x[:] for x in [[val] * n] * m]

def check(lawn):
    for m in xrange(len(lawn)):
        for n in xrange(len(lawn[m])):
            if not (all(lawn[m][n] >= x for x in lawn[m]) or all(lawn[m][n] >= x for x in column(lawn, n))):
                return False
    return True

def main():
    inpath = 'B-large.in'
    outpath = os.path.splitext(inpath)[0] + '.out'
    with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:
        T = int(infile.readline())
        for t in xrange(T):
            M, N = map(int, infile.readline().split())
            lawn = []
            for m in xrange(M):
                lawn.append(map(int, infile.readline().split()))
            outfile.write('Case #%d: %s\n' % (t + 1, 'YES' if check(lawn) else 'NO'))

if __name__ == '__main__':
    main()
