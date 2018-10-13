def valid(n):
    s = str(n)
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            return False
    return True


t = int(input())

for c in range(t):
    n = int(input())
    while not valid(n):
        n -= 1
    print("Case #{}: {}".format(c + 1, n))
