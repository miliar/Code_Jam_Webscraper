a=int(raw_input())
for t in xrange (0,a):
    a1 = int(raw_input())
    for i in xrange(0,4):
        if i == a1-1:
            a2 = raw_input().split()
        else:
            a=raw_input()
    b1 = int(raw_input())
    for i in xrange(0,4):
        if i == b1-1:
            b2 = raw_input().split()
            ans = list(set(a2) & set(b2))
        else:
            a=raw_input()
    if len(ans) == 0:
        print "Case #"+str(t+1)+": Volunteer cheated!"
    elif len(ans) == 1:
        print "Case #"+str(t+1)+": "+ans[0]
    else:
        print "Case #"+str(t+1)+": Bad magician!"
