f = open('D-small-attempt1.in')
cases = int(f.readline())
for case in range(cases):
    omino = f.readline().strip().split()
    omino = [ int(x) for x in omino]
    
    X = omino[0]
    R = omino[1]
    C = omino[2]
    result = "RICHARD"
    if X == 1:
        result = "GABRIEL"
    elif X == 2:
        if R*C % 2 == 0:
            result = "GABRIEL"
    elif X == 3:
        if (R*C%3) == 0 and R*C >= 6 and not (R == 1 and C == 1):
            result = "GABRIEL"
    elif X == 4:
        if R * C >= 12 and R * C % 4 == 0:
            result = "GABRIEL"
    print "Case #" + str(case+1) + ": " + result
