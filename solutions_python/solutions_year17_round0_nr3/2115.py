# Hey there. -- Joshua Allum --
# Does weird bathroom things

TRACE = False

# returns the index and LS and RS values of the left midpoint between l and r
def get_mid(l, r):
    mid = (l + r) // 2
    LS = mid - l - 1
    RS = r - mid - 1
    return [mid, LS, RS]

t = int(input())  # read a line with a single integer
for l in range(1, t + 1):
    # Get N and K
    N, K = [int(s) for s in input().split(' ')]
    if TRACE:
        print('N = {} and K = {}'.format(N, K))
    # Set up stalls list. True if filled, False otherwise
    stalls = []
    stalls.append(True)
    for i in range(1, N + 1):
        stalls.append(False)
    stalls.append(True)
    for k in range(K):
        if TRACE:
            print(stalls)
        left = -1
        midpoints = []
        for i in range(len(stalls)):
            if stalls[i] and (left + 1):
                midpoints.append(get_mid(left, i))
                left = i
            elif stalls[i]:
                left = i
        if TRACE:
            print(midpoints)
        best = max(midpoints, key=lambda x: min(x[1], x[2]))
        midpoints = \
        list(filter(lambda x:
                    min(x[1],x[2]) == min(best[1], best[2]),
                    midpoints))
        if TRACE:
            print(midpoints)
        if len(midpoints) > 1:
            best = max(midpoints, key=lambda x: max(x[1], x[2]))
            if TRACE:
                print(best)
            midpoints = \
            list(filter(lambda x:
                    max(x[1],x[2]) == max(best[1], best[2]),
                    midpoints))
        mid = midpoints[0]
        stalls[mid[0]] = True
        if TRACE:
            print(mid)
    if TRACE:
        print(stalls)
    print('Case #{}: {} {}'.format(l, max(mid[1],mid[2]), min(mid[1],mid[2])))
    

