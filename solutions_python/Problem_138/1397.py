__author__ = 'cheungkt'

import sys


def deceitful_war(dwar, ktemp, ntemp):
    while ntemp:
        if ntemp[0] > ktemp[0]:
            dwar += 1
            ntemp.pop(0)
            ktemp.pop(0)
        elif len(ntemp) > 1:
            a = len(ktemp) - 1
            while a > 0 and (ntemp[0] + .1 == ktemp[a] or ntemp[0] + .01 == ktemp[a] or ntemp[0] + .001 == ktemp[a]):
                a -= 1
            if a == 0:
                if ntemp[0] > ktemp[a]:
                    dwar += 1
            ntemp.pop(0)
            ktemp.pop(a)
        else:
            ntemp.pop(0)
            ktemp.pop(0)
    return dwar


def normal_war(war, ktemp, ntemp):
    while ntemp:
        if len(ntemp) > 1:
            a = 0
            while a < len(ktemp) and ntemp[0] > ktemp[a]:
                a += 1
            if a == len(ktemp):
                war += 1
                ntemp.pop(0)
                ktemp.pop(0)
            else:
                ntemp.pop(0)
                ktemp.pop(a)
        elif ntemp[0] > ktemp[0]:
            war += 1
            ntemp.pop(0)
            ktemp.pop(0)
        else:
            ntemp.pop(0)
            ktemp.pop(0)
    return war


def main():
    with open(sys.argv[1], 'r') as test:
        for i in range(1, int(test.readline()) + 1):
            n = int(test.readline())
            naomi = [float(x) for x in test.readline().split()]
            ken = [float(x) for x in test.readline().split()]
            naomi.sort()
            ken.sort()
            ntemp = naomi[:]
            ktemp = ken[:]
            dwar = deceitful_war(0, ktemp, ntemp)
            ntemp = naomi[:]
            ktemp = ken[:]
            war = normal_war(0, ktemp, ntemp)
            print "Case #%i: %i %i" % (i, dwar, war)


if __name__ == '__main__':
    main()