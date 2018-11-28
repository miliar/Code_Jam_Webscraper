for t in range(1, int(input())+1):
    d, n = map(int, input().split())
    pos = []
    sp = []
    minm = None
    for _ in range(n):
        a, b = input().split()
        pos.append(int(a))
        sp.append(int(b))
    for i in range(n):
        if minm is None:
            minm = (d - pos[i])/sp[i]
        if (d - pos[i])/sp[i] > minm:
            minm = (d - pos[i])/sp[i]
    print("Case #{}: {}".format(t, d/minm))
