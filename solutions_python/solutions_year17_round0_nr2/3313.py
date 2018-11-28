def isTidy(n):
    for i in range(len(n) - 1):
        if n[i] > n[i + 1]:
            r = int(n[i + 1:]) + 1
            return r
    return 0

def findLastTidy(n):
    if n <= 9:
        return n
    while n > 9:
        var = isTidy(str(n))
        if var == 0:
            return n
        else:
            n -= var

N = int(input())
for i in range(N):
    number = int(input())
    print("Case #{}: {}".format(i + 1, findLastTidy(number)))