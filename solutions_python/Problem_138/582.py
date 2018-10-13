def main():
    T = int(raw_input())
    for t in xrange(T):
        N = int(raw_input())
        naomi = [float(x) for x in raw_input().split()]
        ken = [float(x) for x in raw_input().split()]
        naomi.sort()
        ken.sort()
        print "Case #" + str(t+1) + ": " + str(deceitful_war(naomi, ken)) + \
                " " + str(war(naomi, ken))

def deceitful_war(naomi, ken):
    n = len(naomi) - 1
    k = len(ken) - 1
    ret = 0
    while n >= 0 and k >= 0:
        if ken[k] < naomi[n]:
            #if naomi is going to get a point
            n -= 1
            ret += 1
        k -= 1
    return ret

def war(naomi, ken):
    n = len(naomi) - 1
    k = len(ken) - 1
    ret = 0
    while n >= 0 and k >= 0:
        if ken[k] > naomi[n]:
            #if ken is going to get a point
            k -= 1
        else:
            #otherwise naomi will get a point
            ret += 1
        n -= 1
    return ret

if __name__ == "__main__":
    main()
