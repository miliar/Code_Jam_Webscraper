import sys

nums = int(sys.stdin.readline())

for a in range(nums):
    n = int(sys.stdin.readline())

    i = n
    while i >= 0:
        j = str(i)
        l = len(j)
        if l <= 1:
            print('Case #' + str(a + 1) + ": " + j)
            break
        s = 0
        low = 0
        for s in range(l):
            check = int(j[s])
            if check >= low:
                low = check
            else:
                low = -1
                break
        if low >= 0:
            print('Case #' + str(a + 1) + ": " + j)
            break
        else:
            i -= (i % (10 ** (l - s - 1))) + 1

