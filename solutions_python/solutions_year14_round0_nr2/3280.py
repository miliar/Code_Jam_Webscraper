
with open('input') as file:
    # loop over test cases
    T = int(file.readline())    
    for case_nr in xrange(T):
        cps = 2.0 # cookies per second
        time = 0.0
        # target cookie number, costs per farm, cps increase per farm
        C, F, X = [float(i) for i in file.readline().split()]
        # solve problem
        while C/cps + X/(cps+F) < X/cps:
            # it make sense to buy a(nother) farm
            time += C/cps
            cps += F
        else: # not anymore...
            time += X/cps
        print "Case #%i: %.7f" % (case_nr+1, time)
