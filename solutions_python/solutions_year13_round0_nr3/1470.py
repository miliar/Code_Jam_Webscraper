from math import sqrt

def isPal(s): return s == s[::-1]

cases = int(raw_input());
for i in xrange(cases):
    count = 0;
    lo,uo = tuple(map(int, raw_input().split(" ")));
    l = int(sqrt(lo)+1);
    u = int(sqrt(uo)+1);
    for j in xrange(l-1, u+1):
        if isPal(str(j*j)) and isPal(str(j)) and lo <= j*j and j*j <= uo: count += 1;
    print "Case #{}: {}".format(i+1,count);