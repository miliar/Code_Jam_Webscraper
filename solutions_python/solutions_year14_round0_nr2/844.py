
def cookie(c, f, x):
    time = 0
    cps = 2.0
    # compare times
    while (x / cps > (c / cps) + (x / (cps + f))):
        time += c / cps
        cps += f
    return time + x / cps
    
t = input()
for case in range(1,t+1):
    print "Case #%d: %.7f" % (case, cookie(*map(float, raw_input().split())))