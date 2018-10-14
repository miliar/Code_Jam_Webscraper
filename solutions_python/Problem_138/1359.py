def solve(nblocks, naomi, ken):
    deceitful, regular = 0, 0
    nr, nd = [x for x in naomi], [x for x in naomi]
    kr, kd = [x for x in ken], [x for x in ken]
    nr.sort()
    kr.sort()
    nd.sort()
    kd.sort()
    while len(nr) >= 1:
        if nr[0] > kr[len(nr)-1]:
            regular += len(nr)
            nr = []
        elif nr[0] < kr[0]:
            if len(nr) == 1:
                nr = []
            else:
                nr = nr[1:]
                kr = kr[1:]
        else:
            j = 1
            while j >=0 and nr[0] > kr[j]:
                j += 1
            nr = nr[1:]
            kr.remove(kr[j])
    while len(nd) > 0:
        if nd[0] > kd[0]:
            deceitful += 1
            kd = kd[1:]
            nd = nd[1:]
        else:
            x = kd.pop()
            nd = nd[1:]
    return '{0} {1}'.format(str(deceitful), str(regular))  

with open('c:\\python27\\codejam\\outputs.out', 'w') as w, open('c:\\python27\\codejam\\D-large.in') as r:
    cases = int(r.readline())
    for case in range(1, cases+1):
        nblocks = int(r.readline())
        naomi = [float(x) for x in r.readline().split()]
        ken = [float(x) for x in r.readline().split()]
        w.write('Case #{0}: {1}\n'.format(str(case), solve(nblocks, naomi, ken)))

