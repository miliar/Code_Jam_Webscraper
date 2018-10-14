# Greedy algo with book-keeping

T = int(raw_input())
for t in xrange(T):
    cur = 0
    config, K = raw_input().split()
    config = [0 if x == '-' else 1 for x in config]
    K = int(K)
    N = len(config)
    sto = [False] * N
    nflips = 0

    for n in xrange(N-K+1):
        v = (config[n] + cur) % 2
        if v == 0: # need to flip
            cur = (cur + 1) % 2
            sto[n+K-1] = True
            nflips += 1
        else: # no need to flip
            pass

        # unflip if required
        if sto[n]:
            cur = (cur + 1) % 2

    ans = True
    # check remaining if all hapy
    for n in xrange(N-K+1, N):
        v = (config[n] + cur) % 2
        if v == 0:
            ans = False
        
        # unflip if required
        if sto[n]:
            cur = (cur + 1) % 2
    
    if not ans:
        print 'Case #%d: IMPOSSIBLE' % (t+1)
    else:
        print 'Case #%d: %d' % (t+1, nflips)


