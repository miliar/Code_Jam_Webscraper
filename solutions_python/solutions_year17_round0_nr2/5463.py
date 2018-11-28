test = int(input())

def isTidy(num):
    last = 10 ** 19
    while(num > 0):
        currD = num % 10
        if currD > last:
            return False
        else:
            last = currD
            num /= 10
            num = int(num)
    return True

def lastTidy(max):
    lastT = -1
    for i in range(1, max + 1):
        if isTidy(i):
            lastT = i
    return lastT

case = 1
while(test > 0):
    currN = int(input())
    print("Case #{}: {}".format(case, lastTidy(currN)))
    case += 1
    test -= 1

