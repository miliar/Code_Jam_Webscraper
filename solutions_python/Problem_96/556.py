def problem():
    data = file( 'in', 'r' ).readlines()
    test_count = int( data[0] )

    for index, i in enumerate( data[1:test_count+1] ):
        vals = [ int(x) for x in i.split() ]
        googlers = vals[0]
        surprise = vals[1]
        p = vals[2]
        scores = vals[3: googlers + 3 ]
        #print googlers, surprise, p, scores
        googlers_count = 0
        log = []
        for score in scores:
            minv = score / 3
            last = score % 3
            if last == 2:
                a, b, c = minv, minv + 1, minv + 1
            elif last == 1:
                a, b, c = minv, minv, minv + 1
            else:
                a, b, c = minv, minv, minv
           
            if a >= p or b >= p or c >= p:
                googlers_count += 1
            
            if last == 2 and c < p and surprise > 0:
                if minv + 2 >= p:
                    googlers_count += 1
                    surprise -= 1
                    a, b, c = minv, minv, minv + 2

            elif last == 0 and minv + 1 == p and minv > 0 and surprise > 0:
                googlers_count += 1
                surprise -= 1
                a, b, c = minv - 1, minv, minv + 1

            log.append( (a,b,c ) )

        print 'Case #%s: %s' % ( index + 1, googlers_count ) 


if __name__ == "__main__":
    problem()
