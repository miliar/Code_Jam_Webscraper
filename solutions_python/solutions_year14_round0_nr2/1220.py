for case in range(int(raw_input())):
    c, f, x = [i for i in map(float, raw_input().split())]
    t = 0.0
    r = 2.0
    p = x/r
    while x < (p-c/r)*(f+r):
        t += c/r
        r += f
        p = x/r        
        #print p, r, t

    t += p
    print "Case #" + str(case + 1) + ": " + str(round(t, 7))
    #print c,f,x