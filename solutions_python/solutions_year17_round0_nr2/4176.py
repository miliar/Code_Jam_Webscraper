cases = int(raw_input())

for i in range(cases):
    NORI = int(raw_input())
    if len(str(NORI)) == 1:
        print "Case #%d: %d" % (i+1, NORI)
    else:
        for j in xrange(NORI, 0, -1):
            j_list = list(str(j))
            if all(j_list[k] <= j_list[k+1] for k in xrange(len(j_list)-1)):
                print "Case #%d: %d" % (i+1, j)
                break
