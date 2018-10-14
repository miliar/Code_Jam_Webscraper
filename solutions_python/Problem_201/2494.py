def get_LR(wc, i):
    # print wc, i
    left = wc[0:i][::-1]
    l = 0
    for x in left:
        if x == 1:
            break
        l += 1
    # print i, l, left
    right = wc[i + 1:]
    r = 0
    for x in right:
        if x == 1:
            break
        r += 1
    return [l, r]

f = open("C-small-1-attempt0.in", "r").readlines()
T = f.pop(0).strip()
x = 1
output = open("wc1.txt", "w")
for line in f:
    nk = line.strip().split(" ")
    N = int(nk[0])
    K = int(nk[1])
    wc = [1] + [0] * int(N) + [1]

    for person in range(K):
        min_max_LR = None
        max_max_LR = None
        best_index = None
        for stall_index in range(len(wc)):
            if wc[stall_index] == 0:
                LR = get_LR(wc, stall_index)
                # print stall_index, LR
                if min_max_LR is None:
                    min_max_LR = min(LR)
                    max_max_LR = max(LR)
                    best_index = stall_index
                    # print "if not min_max_LR"
                    continue
                if min(LR) == min_max_LR:   
                    # print "if min(LR) == min_max_LR"
                    if max(LR) > max_max_LR:
                        best_index = stall_index
                        max_max_LR = max(LR)
                        # print "if max(LR) > max_max_LR"
                elif min(LR) > min_max_LR:
                    best_index = stall_index
                    max_max_LR = max(LR)
                    min_max_LR = min(LR)
                    # print "elif min(LR) > min_max_LR"
                # print wc, stall_index, best_index, min_max_LR, max_max_LR
            # print
        wc[best_index] = 1
        # print wc, best_index, min_max_LR, max_max_LR, best_index
    print "Case #%s: %s %s" % (x, max_max_LR, min_max_LR)
    output.write("Case #%s: %s %s\n" % (x, max_max_LR, min_max_LR))
    x += 1
output.close()
        # print
        