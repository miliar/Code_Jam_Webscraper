for n in range(int(input())):
    cakes, k = input().split()
    k = int(k)
    f = 0
    for i in range(len(cakes)-k+1):
        if cakes[i] == "-":
            cakes = cakes[:i] + "".join(("-" if p=="+" else "+") for p in cakes[i:i+k]) + cakes[i+k:]
            f += 1
    if "-" in cakes:
        print("Case #%d: IMPOSSIBLE"%(n+1))
    else:
        print("Case #%d: %d"%(n+1,f))
