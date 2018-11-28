tc = int(input())
ca = 1
for xxxxx in range(0, tc):
    inp = int(input())

    while (True):
        cpy = list(str(inp))
        cpy2 = cpy[:]
        cpy2.sort()
        if (cpy == cpy2):
            break
        inp-=1

    print("Case #" + str(ca) + ": " + str(inp))
    ca+=1
