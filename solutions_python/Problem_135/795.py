T = int(raw_input())
for t in xrange(1,T+1):
    r1 = int(raw_input())
    b1 = [set([int(i) for i in raw_input().split()]) for _ in xrange(4)]
    r2 = int(raw_input())
    b2 = [set([int(i) for i in raw_input().split()]) for _ in xrange(4)]
    anses = list(b1[r1-1] & b2[r2-1])
    ans = ""
    if len(anses) == 0: ans = "Volunteer cheated!"
    elif len(anses) == 1: ans = str(anses[0])
    else: ans = "Bad magician!"
    print "Case #%s: %s" % (t,ans)

