m = input()
k = 0
while m > 0:
    """
    c : cookie farm price  
    x : goal
    f : increment
    """
    m -= 1
    k += 1
    c, f, x = [float(i) for i in raw_input().split()]
    curRate = 2.0
    flag = 1
    t = 0.0
    while flag:
        if x/(curRate) <= c/(curRate) + x/(curRate+f):
            t+=x/curRate
            flag = 0
        else:
            t+= c/curRate
            curRate += f 
    print "Case #%d: %.7f"%(k,t)

