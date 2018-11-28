t = int(raw_input())
for case_nr in xrange(1, t + 1):
    n = int(raw_input())
    cnt = 0
    ans = -1
    for i in xrange(1, 5):
        if i == n:
            a = map(int, raw_input().strip().split())
        else:
            raw_input()
    n = int(raw_input())
    for i in xrange(1, 5):
        if i == n:
            b = map(int, raw_input().strip().split())
        else:
            raw_input()
    for i in xrange(0, 4):
        for j in xrange(0, 4):
            if int(a[i]) == int(b[j]):
                cnt += 1
                ans = a[i]
    if cnt == 0:
        print "Case #%d: Volunteer cheated!" % case_nr
    elif cnt == 1:
        print "Case #%d: %d" % (case_nr, ans)
    else:
        print "Case #%d: Bad magician!" % case_nr
