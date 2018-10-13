test = raw_input()
test = int(test)
##print "NUmber of test cases"
#print test
for g in range(1, test+1):
    data = raw_input()
    data = data.rsplit(' ')
    numberg = int(data[0])
    surp = int(data[1])
    count_surp = 1
    minscore = int(data[2])
    scores = []
    answer = 0
    ##print " Input data set is"
    ##print data
    for i in range(0, numberg):
        ##print "***********test case " + str(i)
        scores.append(int(data[i+3]))
        q = scores[i]/3
        d = scores[i]%3

        ##print " quotient %s" % q
        ##print " remainder %s" % d
        if scores[i] == 0:
            ##print " Score is zero"
            pass
            if minscore == 0:
                ##print " Score is zero and minscore is zero, incrementing answer"    
                answer = answer + 1
        else:
            ## 
            if q >= minscore:
                answer = answer + 1
                ##print (" Q greater than miniscore")
            ## quotient is less than the miniscore
            elif (minscore-q <= 1) and ( d == 1 or d == 2):
                    answer = answer + 1
                    ##print " quotient = minscore -1, den = 1 or 2, default calse"
            ##else you have to use surplus
            else:
                if count_surp <= surp:
                    
                    if d == 2 and (minscore - q) <= 2:
                        ##print "Using surplus"
                        answer = answer + 1
                        count_surp = count_surp + 1
                        ##print " remainder is 2 and and minscore -2 == q"
                    elif minscore -1 == q:
                        ##print "Using surplus"
                        answer = answer + 1
                        count_surp = count_surp + 1
                        ##print " remainder is 2 and and minscore -2 == q"
                    else:
                        ##print " Surplus loop un used"
                        pass
                else:
                    ##print "surplus exhausted"
                    pass
    print "Case #%s: %s" %(g, answer)
                
        
