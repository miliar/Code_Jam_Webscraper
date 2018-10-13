def solve(n, li):
    dl = []
    ws = []
    ls = []
    wpl = []
    owpl = []
    oowpl = []
    for i in xrange(n):
        won = filter(lambda x: x == '1', li[i])
        lose = filter(lambda x: x == '0', li[i])
        ws.append(len(won))
        ls.append(len(lose))
        dl.append(len(won) + len(lose))
        wp = float(len(won))/dl[i]
        wpl.append(wp)
    for i in xrange(n):
        xwp = 0.0
        for j in xrange(n):
            if i == j:
                continue
            if li[j][i] == '1':
                xwp += float((ws[j] - 1))/(ws[j] -1 + ls[j])
            elif li[j][i] == '0':
                xwp += float(ws[j])/(ws[j] + ls[j] - 1)
#            else:
#                xwp += float(ws[j])/(ws[j] + ls[j])
        owpl.append(xwp/dl[i])
    for i in xrange(n):
        sum = 0.0
        for j in xrange(n):
            if i == j:
                continue
            if li[j][i] == '1' or li[j][i] == '0':
                sum += owpl[j]
        oowp = float(sum)/dl[i]
        oowpl.append(oowp)
    for i in xrange(n):
        print 0.25 * wpl[i] + 0.5 * owpl[i] + 0.25 * oowpl[i]
        #print "  wp:{0}".format(wpl[i])
        #print "  owp:{0}".format(owpl[i])
        #print "  oowp:{0}".format(oowpl[i])

t = int(raw_input())
for i in xrange(t):
    n = int(raw_input())
    li = []
    for j in xrange(n):
        li.append(raw_input())
    print "Case #{0}:".format(i + 1)
    solve(n, li)
