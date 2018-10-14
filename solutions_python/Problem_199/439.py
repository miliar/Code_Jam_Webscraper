T = int(raw_input())
for t in xrange(1, T+1):
    S,K = map(str, raw_input().split())
    K = int(K)
    a = [0 for _ in xrange(len(S))]
    for i in xrange(len(S)):
        if S[i] == '-': a[i] += 1
    # debug
    # print a
    cnt = 0
    for i in xrange(len(S)-K+1):
        if a[i] % 2 == 1:
            cnt += 1
            for j in xrange(K):
                a[i+j] += 1
        # debug
        # print a
    is_valid = True
    for i in xrange(len(S)):
        if a[i] % 2 == 1:
            is_valid = False
            break
    if is_valid:
        print "Case #" + str(t) + ": " + str(cnt)
    else:
        print "Case #" + str(t) + ": IMPOSSIBLE"
