T = int(raw_input())

for tc in range(1, T+1):
    R, C, W = [int(a) for a in raw_input().strip().split()]
    #print R, C, W
    if C > 2*W:
        if C % W == 0:
            S = R * ( (C/W - 2) + (1 + W) )
        else:
            S = R * ( (C/W - 1) + (1 + W) )
    else:
        S = R * min(C, W+1)
    print "Case #%d: %d" % (tc, S)
