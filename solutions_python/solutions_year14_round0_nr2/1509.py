import sys

def optim(C, F, X, S):
    #time to get to X
    r = 0
    while C/S + X/(S+F)<= X/S:
        r+=C/S
        S+=F
    return r + X/S

fh = open(sys.argv[1])
T = int(fh.readline())
for i in range(T):
    C, F, X = map(float, fh.readline().rstrip().split(" "))
    y = optim(C, F, X, 2.)
    print "Case #{0}: {1}".format(i+1, y)
fh.close()
