def gcjmain1():
    f = open('C:/A-large.in')
    fs = f.read().split('\n')
    out = file("A-large.out", 'w')
    nc = int(fs[0])
    for x in range(nc):
        case = [int(i) for i in fs[x+1].split(' ')]
        ns = case[0]
        bns = ((2 ** ns) - 1)
        snaps = case[1]
        a = (snaps & bns == bns) and "ON" or "OFF"
        #print "%d and %d = Case #%d: %s" % (ns, snaps, x+1, a)
        out.write("Case #%d: %s\n" % (x+1, a))
