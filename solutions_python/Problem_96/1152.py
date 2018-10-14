import sys

def answer(test):
    numlist = [int(a) for a in test.split(' ')]
    N = numlist[0]
    S = numlist[1]
    P = numlist[2]
    totals = numlist[3:]
    over_p = 0;
    surp_over_p = 0;
    for tot in totals:
        div3 = tot/3
        class_ = tot % 3
        if class_ == 0:
            easyly_over_p = (div3 >= P)
        elif class_ in [1,2]:
            easyly_over_p = (div3 + 1 >= P)

        if easyly_over_p:
            over_p += 1
            #print "  ", tot, " can easily be over %i"%P
        else:
            if class_ == 0:
                can_be_over_p = ((div3 + 1 >= P) and (tot > 0))
            elif class_ == 1 :
                can_be_over_p = False
            elif class_ == 2:
                can_be_over_p = (div3 + 2 >= P)
            
            if can_be_over_p:
                surp_over_p += 1
                #print "  ", tot, " can surprisingly be over %i"%P
    #print '  * tot easily: %i' % over_p
    #print '  * tot surprisingly: %i' % surp_over_p
    #print '  * actual surprises: %i' % S
    
    return (over_p + min(surp_over_p, S))

with open(sys.argv[1]) as f:
    with open('output','w') as out:
        for i, test in enumerate(f):
            if i == 0: 
                continue
            out.write("Case #%i: %i\n" % (i, answer(test)))
            #sys.stdout.write("Case #%i: %i\n" % (i, answer(test)))
        
