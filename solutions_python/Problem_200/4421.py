def isTidy(x):
    last = 0
    for dig in x:
        if last > dig:
            return False
        last = dig
    return True

def findTidy(x):
    last = x[0]
    while not isTidy(x):
        for i in range(1, len(x)):
            if last > x[i]:
                x[i - 1] = x[i - 1] - 1
                for j in range(i, len(x)):
                    x[j] = 9
            last = x[i]
    return x

t = input();
for i in range(t):
    n = [eval(x) for x in raw_input()]
    tidy = ""
    tidy.join("1")
    for dig in findTidy(n):
        if tidy is not "" or dig != 0:
            tidy = tidy + str(dig)
    print("Case #{0}: {1}".format(i + 1, tidy))
