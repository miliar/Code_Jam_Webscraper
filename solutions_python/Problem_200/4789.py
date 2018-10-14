def isTiny(n):
    s = str(n)
    for i in range(0,len(s)-1):
        if s[i] > s[i+1]:
            return False
    return True

t = int(input())
for i in range(t):
    n = int(input())
    while not isTiny(n):
        n -= 1
    print("Case #{}: {}".format(i+1, n))