import sys,  os

T = int(sys.stdin.readline())  

for i in range(T):
    num = []
    chk = 0
    size = int(sys.stdin.readline())
    li = sys.stdin.readline().split()
    for x in li:
        num.append(int(x))
        chk ^= int(x)
    if chk != 0:
        ans = 'NO'
    else:
        sum = 0
        min = num[0]
        for x in num:
            sum += x
            if  x < min:
                min = x
        ans = str(sum - min)
    print "Case #%d: " %( i+1) + ans

''''
def add(a,  b):
    ans = 0
    for i in range(20):
        if (a%2 == 0 and b%2 == 0) or (a%2 == 1 and b%2 == 1):
            ans = ans
        elif (a%2 == 0 and b%2 == 1) or (a%2 == 1 and b%2 == 0):
            ans += 2**i
        a = a >> 1
        b = b >> 1
    return ans

print add(50,  10)
print 50 ^ 10'''
