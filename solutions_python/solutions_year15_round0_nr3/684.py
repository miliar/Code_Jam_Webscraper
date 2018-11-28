import sys
import math

f = open(sys.argv[1])
n = int(f.readline())

def pref(w, boolean):
    if boolean:
        if w[0] == "-":
            return w[1:]
        else:
            return "-" + w
    else:
        return w
            
def mult(a,b):
    swpref = False
    if (a[0] == "-" and b[0] != "-") or (a[0] != "-" and b[0] == "-"):
        swpref = True
        
    a = a[-1]
    b = b[-1]
    if a == "1":
        return pref(b, swpref)
    if b == "1":
        return pref(a, swpref)
    if a == b:
        return pref("-1", swpref)
    if (a,b) == ("i","j"):
        return pref("k", swpref)
    if (a,b) == ("i","k"):
        return pref("-j", swpref)
    if (a,b) == ("j","k"):
        return pref("i", swpref)
    if (a,b) == ("j","i"):
        return pref("-k", swpref)
    if (a,b) == ("k","i"):
        return pref("j", swpref)
    if (a,b) == ("k","j"):
        return pref("-i", swpref)

def jkprod(w):
    jset = set()
    kset = set()
    sum = "1"
    for i in range(len(w)):
        sum = mult(sum, w[i])
        if sum == "j":
            jset.add(i+1)
    sum = "1"
    for j in range(len(w)-1, 0, -1):
        sum = mult(w[j], sum)
        if sum == "k":
            kset.add(j)
    if len(kset & jset) > 0:
        return True
    else:
        return False


for t in xrange(1,n+1):
    exp = int(f.readline().strip("\n").split(" ")[1])
    w = f.readline().strip("\n") * exp
    sum = "1"
    found = False
    for x in range(len(w)):
        sum = mult(sum, w[x])
        if sum == "i":

            if jkprod(w[x+1:]):
                print "Case #%d: YES" % (t)
                found = True
                break

    if not found:
        print "Case #%d: NO" % (t)






    

        










