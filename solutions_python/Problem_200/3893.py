def closestTidy(val):
    if len(val) < 2: return val
    newval = map(int, val)
    i=0
    while i < len(newval)-1:
        if (newval[i] > newval[i+1]):
            newval[i] -= 1
            newval = tidyForward(newval, i+1)
            i = -1
        i += 1
    newval = cleanOutput(newval)
    return newval

def tidyForward(val, i):
    while i < len(val):
        val[i] = 9
        i += 1
    return val

def cleanOutput(val):
    while val[0] == 0:
        val.pop(0)
    newval = ""
    for i in xrange(len(val)):
        newval += str(val[i])
    return newval

t = int(raw_input())
for i in xrange(1, t + 1):
    n = raw_input()
    tidy = closestTidy(n)
    print "Case #{}: {}".format(i, tidy)
