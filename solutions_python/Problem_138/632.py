t = int(raw_input())


def manjsi(a, b):
    n = len(a)
    for i in xrange(n):
        if b[i] > a[i]:
            return True
    return False


for case in xrange(1, t+1):
    print "Case #%d:" % case,
    n = int(raw_input())
    naomi = sorted(map(float, raw_input().split()))
    ken = sorted(map(float, raw_input().split()))
    na = naomi[:]
    ke = ken[:]
    for i in xrange(n):
        for j in range(len(ke)):
            if ke[j] > na[i]:
                del ke[j]
                break

    dscore = 0
    while naomi and ken and manjsi(naomi, ken):
        del naomi[0]
        del ken[-1]
    print len(naomi), len(ke)
    #print naomi
    #print ken

