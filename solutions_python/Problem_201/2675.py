t = int(raw_input())

for tst in range(t):
    n, k = map(int, raw_input().split())
    # o+++0
    # 01234
    spots = [False] + [True] * n + [False]
    for person in range(k):
        curr_length = 0
        best_index = None
        best_length = -1
        for i, spot in enumerate(spots):
            if spot:
                curr_length += 1
            else:
                if curr_length > best_length:
                    best_index = i - (curr_length // 2 + 1)
                    best_length = curr_length
                curr_length = 0

        spots[best_index] = False
    res = 0
    left = 0
    for l in range(best_index - 1, -1, -1):
        if spots[l]:
            left += 1
        else:
            break
    right = 0
    for r in range(best_index + 1, n + 1):
        if spots[r]:
            right += 1
        else:
            break
    print "Case #" + str(tst + 1) + ":", max(left, right), min(left, right)
