cache = {}

def time(diners):
    """
        Assume diners is sorted in reverse order.
    """
    if str(diners) in cache:
        return cache[str(diners)]
    if diners[0] <= 3:
        r = diners[0]
        cache[str(diners)] = r
        return r
    else:
        mintime = diners[0]
        for i in range(1, diners[0]//2+1):
            mintime = min(mintime, 1+time(sorted(diners[1:] + [diners[0]-i] + [i], key = lambda x: -x)))
        cache[str(diners)] = mintime
        return mintime
        # return min(diners[0], 1+time(sorted(diners[1:] + [diners[0]//2] + [diners[0]//2 + diners[0]%2], key = lambda x: -x)))
        # return min(
        #         1+time([max(0, x-1) for x in diners]),
        #         1+time(sorted(diners[1:] + [diners[0]//2] + [diners[0]//2 + diners[0]%2], key = lambda x: -x))
        #     )


T = int(input(""))
for testCase in range(T):
    D = int(input(""))
    diners = [int(x) for x in input("").split()]
    diners.sort(key = lambda x: -x)
    cache = {}
    print("Case #%d: %d" % (testCase+1, time(diners)))
