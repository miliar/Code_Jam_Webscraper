T = int(raw_input())
for case in xrange(1,T+1):
    N = int(raw_input())
    if N < 10:
        print "Case #%d: %d" %(case,N)
    else:
        while(True):
            N_str = str(N)
            first = N_str[0]
            for i in xrange(1,len(N_str)):
                second = N_str[i]
                if first > second:
                    break
                first = second
            else:
                print "Case #%d: %d" %(case,N)
                break
            N -= 1