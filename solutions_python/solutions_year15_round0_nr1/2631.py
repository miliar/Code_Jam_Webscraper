T = int(raw_input().strip())


for t in range(1, T+1):
    num_extras = 0
    standing = 0

    S = [int(s) for s in raw_input().strip().split()[1]]

    for s in range(0, len(S)):
        if standing < s and S[s]:
            num_extras += s - standing
            standing += s - standing
        standing += S[s]


    print "Case #%s: %s" % (t, num_extras)