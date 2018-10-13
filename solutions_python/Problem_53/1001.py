import sys
import re

def snapper(n, k):
    snapshotA = [False] * n
    snapshotB = [False] * n
    for i in range(0,k):
        j = 0
        while snapshotA[j] and (j<n-1) :
            j += 1
        for k in range(0,j+1):
            snapshotB[k] = not snapshotA[k]
        snapshotA = snapshotB

    foo = sum(snapshotA)

    return foo == n 


# figure out the number of test cases
s = sys.stdin.readline()
t = int(s.rstrip())

#print t

p = re.compile('\d+')

# start reading test cases
for i in range(1,t+1):
    s = sys.stdin.readline()
    (nn,kk) = p.findall(s)
#    print n
#    print k
    n = int(nn)
    k = int(kk)
    result = "ON" if (snapper(n,k)) else "OFF"
    print "Case #%d: %s" % (i, result)
    

#while True:
#    if not s:
#        break
#    t = s.rstrip()
#    
#    print t

