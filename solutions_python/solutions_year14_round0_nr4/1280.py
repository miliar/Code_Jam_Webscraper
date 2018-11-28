for t in range(input()):
    print "Case #%s:" % str(t + 1),
    n = input()
    N = sorted(map(float, raw_input().split()), reverse=True)
    K = sorted(map(float, raw_input().split()), reverse=True)
    war = 0
    for i in range(n):
        if N[i] > K[i - war]:
            war += 1
    dw = 0
    o = 0
    for i in range(n):
        if N[i - o] > K[i]:
            dw += 1
        else:
            o += 1
    print "%s %s"%(dw, war)