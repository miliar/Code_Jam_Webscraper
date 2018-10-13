def do_jam():
    D, N = raw_input().split(' ')
    D = int(D)
    N = int(N)
    hours=[]
    # print D,N
    for i in xrange(N):
        K, S = raw_input().split(' ')
        K = float(K)
        S = float(S)
        h = float((D - K)/S)
        # print (D-K),S,h
        hours.append(h)

    value = max([float(v) for v in hours])
    r = D/value
    return '{0:.6f}'.format(r)

########
# MAIN #
########
T= int(raw_input())
for i in xrange(1, T + 1):
    print "Case #{}: {}".format(i, str(do_jam()))
