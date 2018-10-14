with open('B-large.in') as file:
    cases = int(file.readline())
    output = open('output.txt','w')
    for c in range(1, cases + 1):
        values = file.readline().split()
        C = float(values[0])
        F = float(values[1])
        X = float(values[2])
        R = float(2)
        r = R + F
        t = 0
        while C/R + X/r < X/R:
            t += C/R
            R = r
            r = R + F
        t += X/R
        output.write("Case #%d: %f\n" % (c, t))
