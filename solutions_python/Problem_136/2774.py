from sys import stdin

def cookies(C,F,X):
    cps = 2.0;
    penality = 0;
    cost_prev = float("inf")
    
    while True:
        cost = penality + X/cps

        if cost_prev <= cost:
            break
        else:
            cost_prev = cost

        penality += C/cps
        cps = cps + F

    return cost_prev
        

num_cases = int(stdin.readline())
for case_index in xrange(1, num_cases+1):

    line = stdin.readline().strip().split(' ')

    C = float( line[0] )
    F = float( line[1] )
    X = float( line[2] )

    
    
    print "Case #" + str(case_index) + ": "+ str(cookies(C,F,X))
