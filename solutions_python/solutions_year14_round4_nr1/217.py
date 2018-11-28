T = int(input())
for I in range(1, T+1):
    n, x = [int(x) for x in input().split()]
    sizes = [int(x) for x in input().split()]
    sizes.sort()
    # find the biggest for smallest:
    good = 0
    for i in range(0, n):
        if (sizes[0] + sizes[i] <= x):
            good = i
    if (good == 0):
        result = n
    else:
        skipped = n - good - 1
        found = 0
        begin = 0
        end = good
        while (begin < end):
            if (sizes[begin] + sizes[end] <= x):
                begin += 1
                end -= 1
                found += 1
            else:
                end -= 1
                skipped += 1
        if begin == end:
            skipped += 1
        result = skipped + found
        
        
    print("Case #%d: %s" % (I, result))
