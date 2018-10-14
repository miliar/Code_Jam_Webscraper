F = 4.0
C = 500.0
X = 2000.0
t = 0.0
# r = 2.0  # cookies per second

"""
def time(C, F, X, r):
    if X/r < C/r+X/(r+F):
        return X/r
    return C/r + time(C, F, X, r+F)
"""

def time(C, F, X, r):
    rate = r
    ttime = 0.0
    while X/rate > C/rate + X/(rate+F):
        ttime += C/rate
        rate += F
    ttime += X/rate
    return ttime
    
#f = file("input.txt","r")
#f = file("B-small-attempt1.in","r")
f = file("B-large.in")
l = f.readlines()
f.close()
fo = file("output.txt","w")
for ll in range(int(l[0])):
    nn = [float(n) for n in l[ll+1].split(' ')]
    fo.write("Case #{0}: {1}\n".format(ll+1,time(nn[0], nn[1], nn[2], 2.0)))

fo.close()


