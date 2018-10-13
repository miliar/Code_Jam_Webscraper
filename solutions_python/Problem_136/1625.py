
f = open('B-large.in', 'r')
results = open('cookie.out', 'w')

T = f.readline()

b = 2 # base cookies per second

for i in range(int(T)):
    params = f.readline().split()

    C = float(params[0]) # cost of farm, in cookies
    F = float(params[1]) # cookies generated per farm per second
    X = float(params[2]) # cookies required for victory


    farms = 0    
    newtime = X / b
    time = X / b + 1 # initialization bullshit
    # print newtime

    while newtime < time:
        time = newtime
        farms += 1

        newtime = time \
                    + C / (2 + F * (farms -1) ) \
                    + X / (2 + F * farms) \
                    - X / (2 + F * (farms - 1) )
                
        #print newtime
        

    # print "Case #", i+1,  time
    results.write("Case #{}: {:.7f}\n".format(i+1, time))
    

results.close()
f.close()
