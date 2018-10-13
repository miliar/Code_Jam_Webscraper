for index, _ in enumerate(range(int(input())), 1):
    c = 0
    for i in range(0, int(input())+1):
        l = sorted([int(x) for x in str(i)])
        t = "".join(str(y) for y in l)
        if i == int(t):
            c = i
        else:
            pass
    print("Case #%s: %s" % (index, c))