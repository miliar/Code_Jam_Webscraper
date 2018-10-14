# May, 8, 2010
# Qualification Round
# "Snapper Chain"

from time import time
from copy import copy

#inpath = "A-sample.in"
#inpath = "A-large.in"
inpath = 'A-small-attempt0.in'
outpath = "A.out"

fin = open(inpath)
fout = open(outpath, 'w')

def Snap(snappers):
    power = True
    for i in range(len(snappers)):
        snapper = snappers[i]
        snappers[i] = not snapper
        power = power and snapper
        if not power:
            break
    return snappers

def Light(N, K):
    snappers = [False]*N
    for i in range(K):
        snappers = Snap(snappers)
    if all(snappers):
        return "ON"
    return "OFF"

timestart = time()
T = int(fin.readline())
for case in range(1, T+1):
    N, K = map(int, fin.readline().split())
    fout.write("Case #%d: %s\n" % (case, Light(N, K)))
    
fin.close()
fout.close()
print "%.4f" % (time() - timestart)
