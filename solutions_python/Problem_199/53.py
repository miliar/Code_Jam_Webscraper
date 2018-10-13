
cases = int(raw_input())
for ctr in xrange(cases):
    sss = raw_input().split(" ")
    pancakes = [True if c == '+' else False for c in sss[0]]
    k = int(sss[1])
    flips = 0
    for index in xrange(len(pancakes) - k + 1):
        if not pancakes[index]:
            flips += 1
            for q in xrange(index, index + k):
                pancakes[q] = not pancakes[q]
    success = True
    for c in pancakes:
        if not c:
            success = False
            break
    if success:
        print "Case #{}: {}".format(ctr + 1, flips)
    else:
        print "Case #{}: {}".format(ctr + 1, "IMPOSSIBLE")
