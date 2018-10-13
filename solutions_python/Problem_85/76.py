from bisect import bisect_left

f = open('input2.txt', 'r')

T = int(f.readline())

for ttt in xrange(1, T + 1):

    line = map(int, f.readline().strip().split())

    L, t, N, C = line[:4]

    A = line[4:]
    Sum = [A[0] * 2]

    for i in xrange(1, N):
        Sum.append(Sum[-1] + A[i % C] * 2)

    Min = Sum[-1]

    if L >= 1:
        
        for k in xrange(N):

            first_boost = bisect_left(Sum, t)

            if k < first_boost:
                continue
            elif k > first_boost:
                Min = min(Min, Sum[-1] - A[k % C])
            else:
                noboost = (t - Sum[k - 1]) / 2 if k > 0 else t / 2
                left = A[k % C] - noboost
                Min = min(Min, t + left + Sum[-1] - Sum[k])

    if L >= 2:

        for k1 in xrange(N):
            for k2 in xrange(k1 + 1, N):

                first_boost = bisect_left(Sum, t)

                if k1 < first_boost:
                    if k2 < first_boost:
                        continue
                    elif k2 > first_boost:
                        Min = min(Min, Sum[-1] - A[k2 % C])
                    else:
                        noboost = (t - Sum[k2 - 1]) / 2 if k2 > 0 else t / 2
                        left = A[k2 % C] - noboost
                        Min = min(Min, t + left + Sum[-1] - Sum[k2])
                elif k1 > first_boost:
                    Min = min(Min, Sum[-1] - A[k1 % C] - A[k2 % C])
                else:
                    noboost = (t - Sum[k1 - 1]) / 2 if k1 > 0 else t / 2
                    left = A[k1 % C] - noboost
                    Min = min(Min, t + left + Sum[-1] - Sum[k1] - A[k2 % C])


    print 'Case #{}: {}'.format(ttt, Min)
