T = int(raw_input())

for i in range(1,T+1):
    print 'Case #%i:' % i,
    N, K = map(int, raw_input().split())
    if (1<<N)-1 == K & ((1<<N)-1):
        print 'ON'
    else:
        print 'OFF'
