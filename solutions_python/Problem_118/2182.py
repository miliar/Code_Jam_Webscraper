import math
def ispalindrome(x):
    if x[::-1] == x:
        return True
    else:
        return False

def nextsquare(low,high):
    squarenum = long(math.ceil(math.sqrt(low))**2)
    yield long(squarenum)
    lastodd = 1+(long(math.sqrt(squarenum))-1)*2
    nextnum = long(squarenum)
    lastodd+=2
    while (nextnum+lastodd)<=high:
        nextnum+=lastodd
        yield nextnum
        lastodd+=2

test_cases = long(raw_input())
for i in range(0,test_cases):
    line = raw_input()
    vals = line.split()
    low = long(vals[0])
    high = long(vals[1])
    nfs = long(0)
    for j in nextsquare(low,high):
        if ispalindrome(str(j)):
            if ispalindrome(str(long(math.sqrt(j)))):
                nfs+=1
    print "Case #"+str(i+1)+": "+str(nfs)

