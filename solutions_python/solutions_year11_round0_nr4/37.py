for trial in range(int(raw_input())):
    N = int(raw_input())
    C = map(int,raw_input().split())
    S = sorted(C)
    p = 0
    for i in range(0,len(C)):
        # if C[i]<C[i-1]: p += 1
        if C[i] != S[i]: p += 1
    print 'Case #%d: %.6f' % (trial+1, p)


# 1/N * SUM(p(x) * x)
