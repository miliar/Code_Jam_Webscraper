def main():
    N = int(raw_input())
    for cur_case in xrange(N):
        cur_case = cur_case + 1
        n,m,X,Y,Z = raw_input().split()
        n = int(n)
        m = int(m)
        X = int(X)
        Y = int(Y)
        Z = int(Z)
        A = []
        for i in xrange(m):
            A.append(int(raw_input()))
        
        limits = []
        for i in xrange(n):
            limits.append(A[i % m])
            A[i % m] = (X * A[i % m] + Y * (i + 1)) % Z

        count = [0] * n
        for i in xrange(n):
            s = 0
            for j in xrange(i):
                if limits[j] < limits[i]:
                    s += count[j]
            count[i] = s + 1
        print 'Case #%d: %d' % (cur_case, sum(count) % 1000000007)


if __name__ == '__main__':
    main()
