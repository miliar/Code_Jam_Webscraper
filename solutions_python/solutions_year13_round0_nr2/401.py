for T in xrange(input()):
    N,M = map(int,raw_input().split())
    L = [j for _ in xrange(N) for j in map(int,raw_input().split())]
    print 'Case #%d:'%(T+1),
    c = N*M
    while c>0:
        h,j = min((h,j) for j,h in enumerate(L))
        if all(l==h or l=='c' for l in L[M*(j/M):j-j%M+M]):
            for j in xrange(j-j%M,j-j%M+M):
                if L[j]==h:
                    c-=1
                    L[j] = 'c'
        elif all(l==h or l=='c' for l in L[j%M::M]):
            for j in xrange(j%M,N*M,M):
                if L[j]==h:
                    c-=1
                    L[j] = 'c'
        else:
            print 'NO'
            break
    else:
        print 'YES'


