t = int(raw_input())
for i in xrange(1, t + 1):
    ac, aj = [int(s) for s in raw_input().split(" ")]
    arrc = []
    arrj = []
    att = []
    for _ in xrange(ac):
        s, t = [int(s) for s in raw_input().split(" ")]
        arrc.append([s, t])
        att.append([0, s, t, t - s])
    for _ in xrange(aj):
        s, t = [int(s) for s in raw_input().split(" ")]
        arrj.append([s, t])
        att.append([1, s, t, t - s])
    att =sorted(att, key = lambda x : x[1])
    if len(att) == 1:
        print "Case #{}: {}".format(i, 2)
    else:
        if att[0][0] == att[1][0]:
            tk = att[0][3] + att[1][3]
            tk += min(att[1][1] - att[0][2], att[0][1] + 1440 - att[1][2])
            if tk > 720:
                print "Case #{}: {}".format(i, 4)
            else:
                print "Case #{}: {}".format(i, 2)
        else:
            print "Case #{}: {}".format(i, 2)

    # print "Case #{}: {}".format(i, switch)