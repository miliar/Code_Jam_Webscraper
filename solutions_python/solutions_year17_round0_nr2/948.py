def isSorted(n):
    if n/10 == 0:
        return True
    prevDigit = n%10
    y = n
    while y !=0 :
        y = y/10
        currentDigit = y%10
        if currentDigit > prevDigit:
            return False
        prevDigit = currentDigit
    return True



def getNearestTidyNumber(n):
    if isSorted(n):
        return n
    y = getNearestTidyNumber((n/10)-1)
    return 10*y + 9

t = int(raw_input())
i = 1
while i <= t:
    n = int(raw_input())
    print "Case #"+str(i)+": " + str(getNearestTidyNumber(n))
    i += 1
