def no_of_friends( sstr):
    aggregation = int(sstr[0])
    no_fr = 0
    for i in xrange(1, len(sstr)):
        no_cur_fr = max(int(i) - aggregation,0)
        aggregation += no_cur_fr + int(sstr[i])
        no_fr += no_cur_fr

    return no_fr



T = input()
for i in xrange(1,T+1):
    sstr = raw_input().split(' ')[1]
    print "Case #%i: %s"%(i,no_of_friends(sstr))
