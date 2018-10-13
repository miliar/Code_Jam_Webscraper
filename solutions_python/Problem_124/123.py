import time, string, numpy as np
import sys
sys.setrecursionlimit(10000)

def p(crust, rem, st, oth, y):
    if st-1 >= y:
        return 1.0
    if rem == 0:
        return 0.0
    if oth == crust:
        return p(crust, rem-1, st+1, oth, y)
    if st == crust:
        return p(crust, rem-1, st, oth+1, y)
    return 0.5 * p(crust,rem-1, st, oth+1, y) + 0.5 * p(crust,rem-1, st+1, oth, y)



t = time.time();
ncases = 2;
f = open('B-small-attempt4.in','r')
fout = open('output.txt','w')
ncases = int(f.readline())
for i in range(ncases):
    # Estimate time left
    print 'ETA: ', (time.time() - t) * ncases / (i+1)

    # read K, N
    line1values = f.readline().split() #First line of data from this case
    N = int(line1values[0])
    X = int(line1values[1])
    Y = int(line1values[2])

    X = abs(X)
    if Y<0:
        pr = 0
    else:
        if X+Y == 0:
            if N>0:
                pr = 1.0
            else:
                pr = 0.0
        else:
            tr = X+Y-1
            mini = tr*(tr+1) / 2
            maxi = (tr+2)*(tr+3) / 2
            if maxi == N:
                pr = 1.0
            elif mini>N:
                pr = 0.0
            else:
                pr = p(X+Y, N-mini, 0, 0, Y)



    #Output decision
    caseResult = str(pr)

    casedesc = 'Case #' + str(i+1) + ': ' + caseResult + '\n'
    fout.write( casedesc )

fout.close()
f.close()
#print "Time per case:", (time.time() - t) / ncases



