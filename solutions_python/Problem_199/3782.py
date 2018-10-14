tc = raw_input ()
tc = int(tc)
test = 0
while tc != 0:
    tc -= 1
    test += 1
    strs, blockSize = raw_input().strip().split()
    strs = list(strs)
    blockSize = int (blockSize)

    times = 0
    for i in range (len(strs)):
        if strs[i] == '-':
            times += 1
            if i + blockSize > len(strs):
                times = "IMPOSSIBLE"
                break
            for j in range (blockSize):
                if strs[i+j] == '-': strs[i+j] = '+'
                elif strs[i+j] == '+': strs[i+j] = '-'
    times = str(times)
    print "Case #%d: %s" % (test, times)