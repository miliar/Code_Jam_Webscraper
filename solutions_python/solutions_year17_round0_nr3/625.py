test_cnt = int(input())

for test in range(1, test_cnt + 1):
    n, k = [int(i) for i in input().split(" ")]
    stalls = dict()
    stalls[n] = 1
    while k > 0:
        n = max(stalls)
        if stalls[n] >= k:
            print("Case #" + str(test) + ": " + str(n // 2) + " " + str((n - 1) // 2))
            k = 0
        else:
            if n // 2 in stalls:
                stalls[n // 2] += stalls[n]
            else:
                stalls[n // 2] = stalls[n]
            if (n - 1) // 2 in stalls:
                stalls[(n - 1) // 2] += stalls[n]
            else:
                stalls[(n - 1) // 2] = stalls[n]
            k -= stalls[n]
            del stalls[n]
