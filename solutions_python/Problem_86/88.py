import sys

# the function to calculate the GCD
def gcd(num1, num2):
    if num1 > num2:
        for i in range(1,num2+1):
            if num2 % i == 0:
                if num1 % i == 0:
                    result = i
        return result

    elif num2 > num1:
        for i in range(1,num1+1):
            if num1 % i == 0:
                if num2 % i == 0:
                    result = i
        return result

    else:
        result = num1*num2/num1
        return result

# the function to calculate the LCM
def lcm(num1, num2):
    result = num1*num2/gcd(num1,num2)
    return result

T = int(sys.stdin.readline())
#print T

def solve(X):
    global num
    for n in num:
        if n >= X:
            if n % X != 0:
                return False
        else:
            if X % n != 0:
                return False
    return True

for t in range(T):
    row = sys.stdin.readline().split(" ")
    N = int(row[0])
    L = int(row[1])
    H = int(row[2])
    num = [int(y) for y in sys.stdin.readline().split(" ")]
#    print N, L, H
#    print num
#    x = reduce(lambda x,y : lcm(x,y), num)
#    print x
    sol = "NO"
    for test in range(L, H+1):
        res = solve(test)
#        print "test", test, res
        if res:
            sol = test
            break
    print "Case #%d: %s" % (t+1, sol)
#    break

