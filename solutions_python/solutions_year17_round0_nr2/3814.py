t = int(input())
def istidy(n):
    m = -1
    for c in str(n):
        i = int(c)
        if i < m:
            return False
        else:
            m = i
    return True
for tst in range(t):
    num = int(input())
    res = 0
    for i in range(num, -1, -1):
        if istidy(i):
            res = i
            break
    print("Case #" + str(tst + 1) + ":", res)
