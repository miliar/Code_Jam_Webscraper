import bisect
T = input()
for t in range(1, T + 1):
    N = input()
    L1 = map(float, raw_input().split())
    L2 = map(float, raw_input().split())
    L1.sort(reverse=True)
    L2.sort(reverse=True)
    L1_idx, L2_idx = 0, 0
    ret1, ret2 = 0, 0
    while 1:
        if L1[L1_idx] > L2[L2_idx]:
            ret1 += 1
            L1_idx += 1
            L2_idx += 1
        else:
            L2_idx += 1
        if L1_idx >= N or L2_idx >= N:
            break
    L2.sort()
    for l1 in L1:
        idx = bisect.bisect(L2, l1)
        if idx < len(L2):
            L2.pop(idx)
        else:
            if l1 > L2.pop(0):
                ret2 += 1

    print "Case #%d: %d %d" % (t, ret1, ret2)