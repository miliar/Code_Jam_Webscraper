from math import ceil, floor, sqrt
def isPal(n):
    k = str(n)
    if n < 10:
        return True
    for i in range(0, len(k)):
        #print [k[i], k[-(i+1)]]
        if k[i] != k[-(i+1)]:
            return False
    return True
def findFairs(a, b):
    a = ceil(sqrt(a))
    b = floor(sqrt(b))
    i = int(a)
    count = 0
    while i <= int(b):
        if isPal(i) :
            #print i*i
            if isPal(i*i):
                count += 1
        i += 1
    return count

T = int(raw_input())
for i in range(0, T):
    l = raw_input()
    l = l.split(" ")
    print "Case #" + str(i+1) +": " + str(findFairs(int(l[0]), int(l[1])))


