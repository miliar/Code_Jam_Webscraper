import sys, math
from decimal import *

def ispalindrome(word):
    if len(word) < 2: return True
    if word[0] != word[-1]: return False
    return ispalindrome(word[1:-1])

t = int(raw_input())
for i in xrange(0,t):
    line = sys.stdin.readline().strip().split(" ")    
    mini = int(line[0])
    maxi = int(line[1])
    maxrooti = int(math.ceil(math.sqrt(maxi)))
    minrooti = int(math.floor(math.sqrt(mini)))
    minpoli = str(minrooti)
    try:
        minpoli = int(minpoli[:int(len(minpoli)/2)])
    except ValueError:
        minpoli = 0
    maxpoli = str(maxrooti)
    try:
        maxpoli = int(maxpoli[:int(len(maxpoli)/2)]) 
    except ValueError:
        maxpoli = 0
#    print "minpol maxpol %d %d minroot maxroot %d %d" % (minpoli, maxpoli, minrooti, maxrooti)
    total = 0
    j = minpoli
    while j <= maxpoli:
        toBeChecked = []
        string = str(j)
        reverse = string[::-1]
        palind = int(string+reverse)
        toBeChecked.append(int(string+reverse))
        for k in range(0,10):
            toBeChecked.append(int(string+str(k)+(reverse if j!=0 else "")))
#        print toBeChecked
        for k in toBeChecked:
            if k>maxrooti or k<minrooti:
                continue
            square = int(math.pow(k, 2))
            if square<mini or square>maxi:
                continue
            isSquarePali = ispalindrome(str(square))
#            print k, square, isSquarePali
            if isSquarePali:
#                print k
                total+=1
        j += 1
    print "Case #%d: %d" % (i+1, total)

