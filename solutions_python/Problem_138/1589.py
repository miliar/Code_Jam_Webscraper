#small gelöst in ~180min
#1 gescheiterter attempt weil alte version von datei o.(\

t = int(input())
for tc in range(1, t+1):
    N = int(input())
    naomi = [float(x) for x in input().split()]
    ken = [float(x) for x in input().split()]
    naomi.sort()
    ken.sort()
    
    kenbup = ken.copy()
    naomibup = naomi.copy()
    z = 0
    while len(naomi) > 0:
        if naomi[-1] > ken[-1]:
            z += 1
            naomi = naomi[:-1]
            ken = ken[1:]
        else:
            naomi = naomi[:-1]
            ken = ken[:-1]
    ken = kenbup
    naomi = naomibup
    y = 0
    while len(naomi) > 0:
        if naomi[0] > ken[0]:
            y += 1
            naomi = naomi[1:]
            ken = ken[1:]
        else:
            naomi = naomi[1:]
            ken = ken[:-1]
            
    print('Case #%i: %i %i' % (tc, y, z))
