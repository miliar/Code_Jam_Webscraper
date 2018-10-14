
T = int(raw_input().strip())
for t in xrange(T):
    (S1, S2) = raw_input().strip().split(" ")
    S_max = int(S1)  # Maximum shyness.
    S = []
    for i in xrange(len(S2)):
        S.append(int(S2[i])) # S[k] is the count with shyness k

    # We need to find the number num_friends to add to S[0]
    # to ensure that everyone stands up.
    # Since S_max <= 1000, we can be sure that inviting 1000 friends
    # will work.
    # Total partial sums:
    TS = []  # TS[i] = S[0] + ... + TS[i]
    for i in xrange(S_max + 1):
        if i == 0:
            TS.append(S[0])
        else:
            TS.append(S[i] + TS[i-1])
    # Now, let's see how many people we need.
    for num_friends in xrange(S_max + 1):
        enough = True
        for i in xrange(1, S_max + 1):
            # shyness level i
            if num_friends + TS[i-1] < i:
                enough = False
                break
        if enough:
            break  # everyone's ok with this setting

    print "Case #%s: %d" % (t+1, num_friends)

# vim: ts=4 sw=4 et smarttab number:
