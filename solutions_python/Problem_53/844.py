import math


def snapper(n,k):
    k = k + 1
    cycle = math.pow(2,n)
    if k % cycle == 0:
        return "ON"
    else:
        return "OFF"


f = open("A-large.in",'r')

t = int(f.readline().strip())

for i in range(1,t+1):
    line = f.readline()
    (n,k) = line.split()
    print "Case #%d: %s" % (i,snapper(int(n),int(k)))

f.close()
