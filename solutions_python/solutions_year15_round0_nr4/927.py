
import fileinput
import numpy

inp = fileinput.input()

cases = int(inp.next()[:-1])
for case in range(cases):
    X, R, C = map(int, inp.next()[:-1].split(" "))
    C_long = max([R,C])
    C_short = min([R,C])
    if X >= 7:
        result = False
    elif X > C_long:
        result = False
    elif numpy.mod(X,2) == 0 and X / 2 > C_short:
        result = False
    elif numpy.mod(X,2) != 0 and X / 2 + 1 > C_short:
        result = False
    elif (R * C == 8) and X == 4:
        result = False
    else:
        if numpy.mod(R*C, X) == 0:
            result = True
        else:
            result = False
    print "Case #%d: %s" % (case+1, "GABRIEL" if result==True else "RICHARD")
     
        