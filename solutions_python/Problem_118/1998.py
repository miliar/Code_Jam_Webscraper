import math

def sqrt(x):
    ans = int(math.sqrt(x)/2)
    if x >= 0:
        while ans*ans < x:
            ans = ans + 1;
        if ans*ans != x:
            return False
        else:
            print(x, "is square!")
            return True
    return None


def palin(x):
    string = str(x)
    while len(string) > 2:
        if string[0] == string[-1]:
            string = string[1:-1]
        else:
            return False
    if len(string) == 2:
        if string[0] == string[1]:
            return True
        else:
            return False
    return True

def fairandsquare(x,y):
    nmax = y
    nmin = x
    fairsq = 0

    while nmin <= nmax:
        if palin(nmin) and sqrt(nmin) and palin(int(math.sqrt(nmin))):
            fairsq = fairsq + 1
        nmin = nmin + 1
    return fairsq


f  = open("C-small-attempt0.in","r")
tests = int(f.readline())
test = 1
lines = f.readlines()
f.close()

w = open('out.txt',"w")
for line in lines:
    if test <= tests:
        vals = line.split()
        count = fairandsquare(int(vals[0]),int(vals[1]))
        w.write("Case #" + str(test) + ": " + str(count) + "\n")
        test = test + 1

w.close()
