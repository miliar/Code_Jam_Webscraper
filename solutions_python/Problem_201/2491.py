t = int(input())

for test_case in range(1, t+1):

    n, k = [int(x) for x in input().strip().split()]

    stalls = [0, n+1]

    for person in range(0, k):

        gaps = {}
        for i in range(1, len(stalls)):
            gaps[(stalls[i-1], stalls[i])] = abs(stalls[i-1] -stalls[i])

        max_diffs = [x for x, v in gaps.items() if v == max(gaps.values())]
        min_max_diff = min(max_diffs, key=lambda x: x[0])


        s = (min_max_diff[0] + (min_max_diff[1] - min_max_diff[0]) // 2)
        stalls.append(s)
        stalls.sort()

        if person == k - 1:
            idx = stalls.index(s)
            ls, rs = stalls[idx-1], stalls[idx+1]
            ls, rs = s - ls - 1, rs - s - 1
            print("Case #{}: {} {}".format(test_case, max(ls, rs), min(ls, rs)))

