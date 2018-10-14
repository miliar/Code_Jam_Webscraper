import sys

def isTidy(num):
    last = '0'
    for x in num:
        if x == '0':
            return False
        if x < last:
            return False
        last = x
    return True

def getLargest(num):
    buffer = num
    while(not isTidy(str(buffer))):
        buffer -= 1
    return buffer

n = int(sys.stdin.readline())

for i in range(n):
    num = int(sys.stdin.readline().strip())
    print("Case #" + str(i + 1) + ": " + str(getLargest(num)))
