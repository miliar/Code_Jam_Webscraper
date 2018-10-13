inp = open('B-large.in')
out = open('B-large.out', 'w')
T = int(next(inp))
initRate = 2
for test in range(T):
    C,F,X = [float(x) for x in next(inp).split()]
    cookies = 0
    rate = initRate
    timeElapsed = 0
    while cookies < X:
        remaining = X - cookies
        t_est_now = remaining / rate
        t_to_farm = (C - cookies) / rate
        t_est_with_farm = X / (rate + F) + t_to_farm
        if t_est_with_farm < t_est_now: #buy a farm
            timeElapsed += t_to_farm
            cookies = 0
            rate += F
        else: #don't buy a farm until...forever
            timeElapsed += t_est_now
            cookies = X
    out.write("Case #" + str(test + 1) + ": " + str(timeElapsed) + "\n")

inp.close()
out.close()
            
        
