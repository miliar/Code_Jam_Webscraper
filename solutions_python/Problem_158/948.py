import os
import sys


f = open(os.path.join(sys.path[0], 'D-small-attempt0.in'))
out = open(os.path.join(sys.path[0], 'D-small-attempt0.out'), 'w')

T = int(f.readline().strip())
for t in xrange(T):
    X, R, C = (int(i) for i in f.readline().strip().split())
    result = ""
    if X == 1:         
        result = "GABRIEL"
    if X == 2:
        result = "GABRIEL" if (R * C) % 2 == 0 else "RICHARD"
    if X == 3:
        if (R * C) % 3 == 0 and ((R >= 3 and C >= 2) or (R >= 2 and C >= 3)):
            result = "GABRIEL" 
        else:
            result = "RICHARD"
    if X == 4:
        if (R * C) % 4 == 0 and ((R >= 3 and C >= 4) or (R >= 4 and C >= 3)):
            result = "GABRIEL" 
        else:
            result = "RICHARD"
    
    result = "Case #{0}: {1}".format(t + 1, result)
    out.write(result + "\n")
    print result

out.close()
