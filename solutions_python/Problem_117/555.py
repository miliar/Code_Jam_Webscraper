
def solve(N, M, A):
    H_set = set()
    for row in A:
        H_set.update(row)
    H = sorted(H_set)
    for idx, val in enumerate(H):
        while any(val in row for row in A):
            found = False
            for i in xrange(N):
                line = A[i]
                if all(x <= val for x in line) and any(x == val for x in line):
                    for j in xrange(M):
                        A[i][j] = -1
                    found = True
            for j in xrange(M):
                line = [A[i][j] for i in xrange(N)]
                if all(x <= val for x in line) and any(x == val for x in line):
                    for i in xrange(N):
                        A[i][j] = -1
                    found = True
            if not found:
                return "NO"
        if idx == len(H) - 1:
            break
        for i in xrange(N):
            for j in xrange(M):
                if A[i][j] < 0:
                    A[i][j] = H[idx + 1]
    return "YES"

def main(f):
    T = int(f.readline())
    for i in xrange(T):
        N, M = map(int, f.readline().split(' '))
        A = []
        for j in xrange(N):
            row = map(int, f.readline().split(' '))
            A.append(row)
        print 'Case #%d:' % (i + 1), solve(N, M, A)

if __name__ == '__main__':
    import sys
    main(sys.stdin)
