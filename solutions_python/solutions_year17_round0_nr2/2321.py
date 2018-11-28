

def tidy(n):
    if n < 10:
        return n
    n = numToArray(n)
    currDigit = len(n) - 2
    count = 0
    while True:
        if (isTidy(arrayToNum(n[currDigit:currDigit+2]))):
            if currDigit == 0:
                break
            currDigit -= 1
        else:
            n = n[:currDigit] + numToArray(arrayToNum(n[currDigit:currDigit+2]) - 1,n[currDigit:currDigit+2]) + n[currDigit+2:]
    return backTidy(arrayToNum(n))


def backTidy(n):
    n = numToArray(n)
    for i in range(1,len(n)):
        if n[i] < n[i-1]:
            n[i] = n[i-1]
    return arrayToNum(n)



def numToArray(n,before=None):
    n = str(n)
    a = []
    for digit in n:
        a += [int(digit)]
    if before != None and len(a) != len(before):
        a = [0] + a
    return a

def arrayToNum(a):
    a = map(str,a)
    a = "".join(a)
    a = int(a)
    return a

def isTidy(n):
    a = numToArray(n)
    prev = a[0]
    for i in range(1,len(a)):
        if a[i] < prev:
            return False
        prev = a[i]
    return True

def naiveTidy(n):
    for i in range(n,0,-1):
        if isTidy(i):
            return i


def parse(fi):
    f = open(fi,"r")
    return map(lambda x: x[:-1],f.readlines())

def problem():
    data = parse("tidynumbers/input.txt")
    for i in range(1,len(data)):
        print "Case #" + str(i) + ": " + str(tidy(int(data[i])))

problem()
