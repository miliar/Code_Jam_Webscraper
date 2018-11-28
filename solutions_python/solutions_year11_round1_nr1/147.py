d = {i:min([j for j in range(1,101) if i*j/100.0 == round(i*j/100.0)]) for i in range(1,101)}
d[0] = 0
for case in xrange(input()):
    n, pd, pg = [int(x) for x in raw_input().split()]
    if (pg == 100 and pd < 100) or (pg == 0 and pd > 0) or n < d[pd]:
        m = 'Broken'
    else:
        m = 'Possible'
    print "Case #%d:" % (case+1), m
