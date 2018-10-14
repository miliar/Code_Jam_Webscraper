#/bin/python
import sys, math

def pa(a):
    if len(a) <= 1:
        return True
    if a[0] == a[-1]:
        return pa(a[1:-1])
    return False

def calculate(a, b):
    count = 0
    for i in xrange(a, b+1):
        s = math.sqrt(i)
        if s == int(s) and pa(str(i)) == True and pa(str(int(s))) == True:
            count = count + 1 
    return count

num = int(sys.stdin.readline())

count = 1

while num > 0:
    a, b = [int(x) for x in sys.stdin.readline().strip().split(" ")]
    N = calculate(a, b) 
    result = "Case #" + str(count) + ": " + str(N)
    print result
    num = num - 1
    count = count + 1

