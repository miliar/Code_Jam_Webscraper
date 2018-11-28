def solve():
    N = [int(i) for i in list(raw_input())]
    n = len(N)

    # print N

    nontidy_idx = -1

    for i in xrange(n-1):
        if N[i] > N[i+1]:
            nontidy_idx = i
            break

    # print 'idx: %d' % nontidy_idx

    while nontidy_idx > 0 and N[nontidy_idx] == N[nontidy_idx-1]:
        nontidy_idx -= 1

    # print 'idx: %d' % nontidy_idx

    # should_tidy = False
    # for i in xrange(nontidy_idx, n):
    #     if N[nontidy_idx] > N[i]:
    #         should_tidy = True

    if nontidy_idx != -1:
        N[nontidy_idx] = N[nontidy_idx] - 1
        for i in xrange(nontidy_idx+1, n):
            N[i] = 9

    return int(''.join([str(i) for i in N]))

for case in xrange(int(input())):
    print 'Case #%d: %s' % (case+1, solve())
