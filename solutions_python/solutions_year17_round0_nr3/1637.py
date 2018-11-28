# Problem C. Bathroom Stall

def floorPow2(n): # n is the nth person that goes in 
    prev = 1
    curr = 1
    while n >= curr:
        prev = curr
        curr *= 2

    return prev


def getvalue(origVal, n, rightSide):
    if n == 0:
        return origVal
    lastpow = floorPow2(n)
    lastRight = False

    if lastpow == 1: # this the base case
        lastVal = 0
    else:
        div = lastpow // 2
        lastVal = div + ((n-lastpow) % div)
        lastSide = (n - lastpow) // div
        if lastSide == 1:
            lastRight = True

    v = getvalue(origVal, lastVal, lastRight)

    if rightSide:
        if v == 0:
            return 0
        else:
            return (v-1)//2
    else:
        return v // 2


test = int(input(""))
for i in range(1, test+1):
    nkstr = input("")
    n = int(nkstr[0:nkstr.find(' ')])
    k = int(nkstr[nkstr.find(' ') + 1:])
    print("Case #" + str(i) + ": ", getvalue(n,k,False), getvalue(n,k,True))





