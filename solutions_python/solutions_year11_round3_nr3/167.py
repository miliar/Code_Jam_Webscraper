T = input()
for testcase in range(T):
    [N,L,H] = [int(x) for x in raw_input().split()]
    notes = [int(x) for x in raw_input().split()]
    
    for x in range(L,H+1):
        for f in notes:
            if (f%x != 0) and (x%f != 0):
                break
        else:
            print "Case #%i:" % (testcase+1), x
            break
    else:
        print "Case #%i:" % (testcase+1), 'NO'
    
                

    

    

