def isTidy(n):
    st = str(n)
    for x in range(len(st)-1):
        if int(st[x+1]) < int(st[x]):
            return False
    return True

tests = int(input())

for z in range(tests):
    x = int(input())
    while not isTidy(x):
        x -= 1
    print("Case #{}: {}".format(z+1, x))