for T in xrange(input()):
    l = input()
    N = sorted(map(float,raw_input().split()))
    K = sorted(map(float,raw_input().split()))
    n1 = n2 = 0
    j = 0
    for i in xrange(l):
        if N[i]>K[j]:
            n1+=1
            j+=1
    j = l-1
    for i in xrange(l-1,-1,-1):
        if N[i]>K[j]:
            n2+=1
        else:
            j-=1
    x = y = 0
    print "Case #%d: %d %d"%(T+1,n1,n2)
