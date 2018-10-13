t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    tot = 0
    n = [int(s) for s in raw_input()]  # read a list of integers, 2 in this case
    outNum = list(reversed(n))
    for idx, dig in enumerate(outNum):
        if idx < len(outNum) - 1:
            if outNum[idx] < outNum[idx+1]:
                for j in range(0,idx+1):
                    outNum[j] = 9
                outNum[idx+1] -= 1

    for idx, dig in enumerate(outNum):
        tot = tot + (dig * 10**idx)
    print "Case #{}: {}".format(i, tot)