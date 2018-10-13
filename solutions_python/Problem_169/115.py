from time import clock
import sys
import numpy as np
# stderr isn't piped to a.out when we do  (py3 a.py < a.in) > a.out
print = lambda *s: sys.stderr.write(" ".join(str(m) for m in s)+"\n")

#---------------------------------------------

"""

for n = 2, we have to solve the formulas given in the problem statement

    V0+V1 = V
    (V0X0 + V1X1) / (V0 + V1) = X

    OMG! SYSTEM OF EQUATIONS! :O
        OMG! my linear algebra course is useful!

    well, sort of.

    V0+V1 = V
    (V0X0 + V1X1) = (V0 + V1) X
    V0 X0 + V1 X1 = V0 X + V1 X
    V0 X0 - V0 X + V1 X1 - V1 X = 0
    V0 (X0-X) + V1 (X1-X) = 0

    and we know all X's! perfect!


hm, for bigger n this might not be a linalg problem
    but an optimisation problem

well, are there multiple solutions for bigger ns?
    yes. consider two fast 20, 40 pumps and a slow 30 one when X = 30

"""

def run(data):

    v, x, pumps = data
    print(v, x, pumps)

    # we only have one pump
    try:
        pumps[1]
    except:
        print("  ONE PUMP  ")
        if x - 0.0000001 < pumps[0][1] < x + 0.0000001:
            return "%.9f" % (v / pumps[0][0])
        return "IMPOSSIBLE"

    # both can pump
    if pumps[0][1] == pumps[1][1]:
        print(" THAT         CASE              ")
        if (x - 0.0000001 < pumps[0][1] < x + 0.0000001):
            return "%.9f" % (v / (pumps[0][0]+pumps[1][0]))
        return "IMPOSSIBLE"


    # "normal" case
    a = np.array( [[1,1], [ pumps[0][1] - x, pumps[1][1] - x]] )
    b = np.array( [v,0] )

    sol = np.linalg.solve(a, b)

    if sol[0] < 0 or sol[1] < 0:
        return "IMPOSSIBLE"

    return "%.9f" % max(sol[0] / pumps[0][0], sol[1] / pumps[1][0])


#---------------------------------------------

def read_case():

    cnt, v, x = [float(n) for n in input().split()]

    pumps = []
    for i in range(int(cnt+.1)):
        pumps.append([float(n) for n in input().split()])

    return (v, x, pumps)

for i in range(int(input())):
    outstr = "Case #"+str(i+1)+": "+str(run(read_case()))
    print(outstr+" @ t="+str(clock()))
    sys.stdout.write(outstr+"\n")
