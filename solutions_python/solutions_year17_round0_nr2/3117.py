def t(n):
    l = len(str(n))
    for i in range(1, l):
        if n == 0:
            break
        a = n // 10 ** (l - 1)
        b = (n // 10 ** (l - 2)) % 10
        if a > b:
            return False, i
        l = l - 1
        n = n % (10 ** l)
    return True, 0

def f(n):
    while True:
        l = len(str(n))
        a = n // 10 ** (l - 2)
        r, i = t(n)
        if r:
            break
        d = 10 ** (l - i)
        n = n // d * d - 1
    return n

for i in range(int(input())):
    n = int(input())
    print("Case #" + str(i+1) + ": " + str(f(n)))
