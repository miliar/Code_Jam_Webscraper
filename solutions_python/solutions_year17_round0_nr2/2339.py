import string

def digitCount(n):
    # returns the number of digits in n
    return len(str(n))

def kthDigit(n,k):
    # gets the kth digit of n, starting at 0, from the left
    d = digitCount(n)
    return (n // (10**(d-k-1))) % 10

def isTidy(n):
    for j in range(digitCount(n) - 1):
        if kthDigit(n,j) > kthDigit(n, j+1):
            return False
    return True

def case(i):
    k = int(input())
    while(not isTidy(k)):
        for j in range(digitCount(k) - 1):
            if kthDigit(k,j) > kthDigit(k, j+1):
                k = k - (k % (10**(digitCount(k) - j - 1))) - 1
                break
    print("Case #{}: {}".format(i, k))

t = int(input())
for i in range(1,t+1):
    case(i)