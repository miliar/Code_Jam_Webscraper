def search(x, l):
    mindiff = 1.0     # Difference between two weights is no more than 1
    minindex = -1
    for i, val in enumerate(l):
        d = val - x
        if val > x and d < mindiff:
            mindiff = d
            minindex = i
    if minindex >= 0:
        del l[minindex]
        return (l, False)
    else:
        return (l, True)

def war(naomi, ken):
    nk = ken
    points = 0
    for x in naomi:
        (nk, nwin) = search(x, nk)
        if nwin:
            points += 1
    return points

def deceit_war(naomi, ken, l):
    nl,nr = 0, l-1
    score = 0
    naomi.sort()
    ken.sort(reverse=True)
    for k in ken:
        if k > naomi[nr]:
            nl += 1
        else:
            nr -= 1
            score += 1
    return score

f = open("D-large.in", 'r')
t = int(f.readline().strip())
for i in range(t):
    n = int(f.readline().strip())
    naomi = [float(x) for x in f.readline().strip().split(' ')]
    ken = [float(x) for x in f.readline().strip().split(' ')]
    print "Case #%d: %d %d" % (i+1, deceit_war(naomi, ken, n), war(naomi, ken))