#!/usr/bin/python

inp = open('large.in', 'r')
out = open('out', 'w')

times = int(inp.readline().strip())

p = 0

while p < times:
    result = ""
    N = int(inp.readline().strip())
    naomi = [float(x) for x in inp.readline().strip().split(' ')]
    ken = [float(x) for x in inp.readline().strip().split(' ')]

    war_naomi = list(naomi)
    war_naomi = sorted(war_naomi, reverse=True)
    war_ken = list(ken)
    war_ken = sorted(war_ken)

    war_points = 0
    for n in war_naomi:
        i = 0
        ind = 0
        le = len(war_ken)
        while i < le:
            kn = war_ken[i]
            if kn > n:
                ind = i
                break
            i = i + 1
        kn = war_ken.pop(ind)
        if n > kn:
            war_points = war_points + 1

    dwar_naomi = list(naomi)
    dwar_naomi = sorted(dwar_naomi, reverse=True)
    dwar_ken = list(ken)
    dwar_ken = sorted(dwar_ken, reverse=True)

    dwar_points = 0
    for i in xrange(0, N):
        nn = dwar_naomi[0]
        kn = dwar_ken[0]
        if nn > kn:
            dwar_naomi.pop(0)
            dwar_ken.pop(0)
            dwar_points = dwar_points + 1
        else:
            dwar_naomi.pop(-1)
            dwar_ken.pop(0)
    

    outLine = "Case #" + str(p+1) + ": " + str(dwar_points) + " " + str(war_points)
    print outLine
    out.write(outLine + "\n")
    p = p + 1

inp.close()
out.close()

