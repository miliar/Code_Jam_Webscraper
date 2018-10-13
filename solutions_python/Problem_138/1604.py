import sys
import bisect

def deceit(naomi, ken):
    result = 0
    while naomi:
        if naomi[0] < ken[0]:
            naomi = naomi[1:]
            ken = ken[0:-1]
        else:
            naomi = naomi[1:]
            ken = ken[1:]
            result += 1
    return result

def optimal(naomi, ken):
    result = 0
    while naomi:
        if naomi[-1] > ken[-1]:
            naomi = naomi[0:-1]
            ken = ken[1:]
            result += 1
        else:
            tmp = naomi[-1]
            naomi = naomi[0:-1]
            idx = bisect.bisect_right(ken, tmp)
            ken = ken[0:idx] + ken[idx+1:]
    return result

lines = sys.stdin.readlines()
t = int(lines[0])
for i in range(1, t + 1):
    naomi = map(float, lines[i * 3 - 1].split())
    ken = map(float, lines[i * 3].split())
    naomi.sort()
    ken.sort()
    #print naomi
    #print ken
    optimal(naomi, ken)
    print "Case #%d:"%i, deceit(naomi, ken), optimal(naomi, ken)