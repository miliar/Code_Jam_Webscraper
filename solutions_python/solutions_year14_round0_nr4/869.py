#! /usr/bin/env python

def solve(naomi, ken):
    naomi.sort()
    ken.sort()

    return deceit(naomi[:], ken[:]), fair(naomi, ken)


def deceit(naomi, ken):
    score = 0
    while naomi:
        if naomi[-1] > ken[-1]:
            naomi.pop()
            score += 1
        else:
            naomi.pop(0)
        ken.pop()
    return score


def fair(naomi, ken):
    score = 0
    while naomi:
        if naomi[-1] > ken[-1]:
            naomi.pop()
            ken.pop(0)
            score += 1
        else:
            def kens(n):
                return first(k for k in ken if k > n)

            n = naomi[-1]
            k = kens(n)
            n = first(n for n in naomi if kens(n) == k)
            ken.remove(k)
            naomi.remove(n)
    return score


def first(it):
    try:
        return it.next()
    except StopIteration:
        return None


def main():
    t = input()
    for i in xrange(1, t + 1):
        n = input()
        naomi = map(float, raw_input().split())
        ken = map(float, raw_input().split())
        print 'Case #{0}: {1} {2}'.format(i, *solve(naomi, ken))


if __name__ == '__main__':
    main()
