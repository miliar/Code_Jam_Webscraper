from sys import stdin
from bisect import bisect_left, bisect_right

T = int(stdin.readline())

for i in xrange(1, T+1):
    N = int(stdin.readline())
    naomi = map(float, stdin.readline().split())
    ken = map(float, stdin.readline().split())
    naomi.sort()
    ken.sort()
    naomi_war = 0
    naomi_dwar = 0
    naomid = list(naomi)
    kend = list(ken)
    for _ in xrange(N):
        Cn = naomi[0]
        Ck = bisect_right(ken, Cn)
        if Ck == len(ken):
            naomi_war += 1
            ken = ken[1:]
        else:
            del(ken[Ck])
        naomi = naomi[1:]

        if naomid[-1] > kend[0]:
            naomi_dwar += 1
            Ck = kend[0]
            Cn = bisect_left(naomid, Ck)
            kend = kend[1:]
            del(naomid[Cn])
        elif len(kend) == 1:
            pass
        else:
            del(kend[-1])
            del(naomid[0])
        
    print 'Case #{0}: {1} {2}'.format(i, naomi_dwar, naomi_war)
