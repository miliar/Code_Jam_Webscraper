n = int(raw_input())
for i in xrange(n):
    goal,m = [int(s) for s in raw_input().split(" ")]
    max_time = 0
    for j in xrange(m):
        o,p = [int(t) for t in raw_input().split(" ")]
        max_time = max((goal - o)/(p*1.0), max_time)

    annie = goal/max_time
    print "Case #{}: {:.20f}".format(i+1, annie)
