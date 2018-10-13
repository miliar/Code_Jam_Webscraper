
import time

T = int(raw_input())

for t in range(0,T):
    C, F, X = [float(a) for a in raw_input().split()]
    bt = 0
    xt = None
    f = 0
    xd = X/2
    sol = 0
    p_sol = None
    while(1):
        bt = bt + (C/(2+f))
        f = f+F
        xt = (X)/(2+f)
        sol = bt + xt
        if xd < sol:
            if xd < bt:
                # xd is the solution
                print "Case #%d: %.7f" %(t+1, xd)
                break;
            else:
                # look for more
                pass
        if p_sol:
            if p_sol < sol:
                if p_sol < xd:
                    # p_sol is solution
                    print "Case #%d: %.7f" %(t+1, p_sol)
                    break;
                else:
                    # xd is solution
                    print "Case #%d: %.7f" %(t+1, xd)
                    break;
        p_sol = sol

        
        
