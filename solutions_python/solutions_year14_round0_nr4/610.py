def deceitful_war(naomi, ken):
    naomi_pts = 0

    for n in naomi:
        if n > ken[0]:
            ken = ken[1:]
            naomi_pts += 1
        else:
            ken = ken[:-1]

    return naomi_pts

def war(naomi, ken):
    naomi_pts = 0
    for n in naomi:
        ken_wins = False
        for k in ken:
            if k > n:
                ken_wins = True
                ken.remove(k)
                break
        if ken_wins:
            continue
        else:
            naomi_pts += 1
            ken = ken[1:]

    return naomi_pts

with open("D-large.in") as f:
    for case in xrange(int(f.readline())):
        f.readline()
        naomi = sorted([float(x) for x in f.readline().split(" ")])
        ken = sorted([float(x) for x in f.readline().split(" ")])

        print "Case #%d: %d %d" % (case + 1, deceitful_war(naomi, ken), war(naomi, ken))
