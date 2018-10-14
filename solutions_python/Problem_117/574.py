import sys

def get_column(A, col):
    res = []
    for row in A:
        res.append(row[col])
    return res

def has_larger(pos, vec):
    for i in range(0, len(vec)):
        if i != pos and vec[i] > vec[pos]:
            return True
    return False

def test(A):
    if len(A) == 1 or len(A[0]) == 1:
        return 'YES'
    for i in range(0, len(A)):
        for j in range(0, len(A[0])):
            if has_larger(j, A[i]) and has_larger(i, get_column(A, j)):
                return 'NO'
    return 'YES'

with open(sys.argv[1]) as f:
    T = int(f.readline())
    for case in range(1,T+1):
        (N, M) = map(int, f.readline().split(' '))
        A = []
        for line in range(1,N+1):
            A.append(map(int, f.readline().split(' ')))
        print 'Case #%i: %s' % (case, test(A))
