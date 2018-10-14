def solvePalindrome(file):
    f = open(file, 'r')
    i = 0
    for line in f:
        #print line
        if i == 0:
            num_tests = line
            i += 1
            #print num_tests
        else:
            interval = line.split(' ')
            #print interval
            lower = int(interval[0])
            #print lower
            upper = int(interval[1])
            #print upper
            findAmount(lower, upper, i)
            i += 1
    return 0

def findAmount(low, high, testno):
    #print range(low, high)
    amount = 0
    i = low
    while i <= high:
        if checkPalindrome(i):
            if square(i):
                #print i
                amount += 1
        i += 1
    print 'Case #'+str(testno)+': '+str(amount)

def checkPalindrome(number):
    if int(str(number)[::-1]) == number:
        return True
    else:
        return False

def square(num):
    checknum = round(num**0.5, 0)
    if checknum**2 == num:
        if checkPalindrome(int(checknum)):
            return True
    return False
