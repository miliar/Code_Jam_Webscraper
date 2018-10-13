t = input()

for case in range(1, t + 1):
    numblks = input()
    nao = [float(x) for x in raw_input().split()]
    ken = [float(x) for x in raw_input().split()]
    nao.sort()
    ken.sort()
    nao.reverse()
    ken.reverse()
    # ken goes first
    sck = 0
    nk = list(nao)
    kk = list(ken)
    for i in range(numblks):
        if nk[0] > kk[0]:
            sck += 1
            kk.pop(0)
            nk.pop(0)
        else:
            kk.pop(0)
            nk.pop()
    # nao goes first
    scn = 0
    for i in range(numblks):
        if ken[0] > nao[0]:
            ken.pop(0)
            nao.pop(0)
        else:
            scn += 1
            nao.pop(0)
            ken.pop()
    print "Case #%d: %d %d" % (case, sck, scn)
