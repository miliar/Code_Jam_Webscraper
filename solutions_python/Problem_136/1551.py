'''
Created on 12 apr 2014

@author: algestam
'''

def solve(cost, extra, target):
    rate = 2
    time = 0.0
    
    while(True):
        if (target / rate < (cost/rate + target/(rate+extra))):
            time += target/rate
            break
        else:
            time += cost/rate
            rate += extra
    
    return time

for case in xrange(input()):
    C, F, X = [float(v) for v in raw_input().split()]
    
    res = solve(C, F, X)

    print "Case #%i: %.7f" % (case+1, res)
    