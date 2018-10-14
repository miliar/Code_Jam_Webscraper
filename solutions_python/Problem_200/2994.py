def check(digits):
    c=[]
    f=str(digits)
    for digit in f:
        c.append(int(digit))
    n = len(f)
    for i in range (n-1):
        if c[i] > c[i+1]:
            return False
    return True

t = int(input())
for i in range(t):
    n = int(input())
    k = 0
    for j in range(1,n + 1):
        if check(j) == True:
            k = j
        if j == n:
            print("Case #" + str((i + 1)) + ": " + str(k))

