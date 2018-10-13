def isTidy(n):
    prev = 0
    for i in range (0, len(n)):
        d = int(n[i])
        if prev > d:
            return i - 1
        prev = d
    return -1


def lower(n, ind):
    l = list(n)
    for i in range(ind, len(l)):
        if i == ind:
            l[i] = str(int(l[i]) - 1)
        else:
            l[i] = '9'
    return ''.join(l)


def findLargestTidy(n):
    while True:
        x = isTidy(n)
        if x == -1:
            return n
        else:
            n = lower(n, x)


t = int(input())
for i in range(1, t + 1):
    n = input()
    print("Case #{}: {}".format(i, int(findLargestTidy(n))))
