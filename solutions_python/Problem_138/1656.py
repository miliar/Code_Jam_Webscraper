def war(naomi, ken):
    i = 0
    score = 0
    for n in ken:
        if n > naomi[i]:
            score += 1
            i += 1

    return len(ken) - score


def dec(naomi, ken):
    N = len(ken)
    i = N - 1
    score = 0
    for j in reversed(range(N)):
        if naomi[i] > ken[j]:
            score += 1
            i -= 1

    return score


def solve(naomi, ken):
    naomi = sorted(naomi)
    ken = sorted(ken)

    warnaomi = war(naomi, ken)
    decnaomi = dec(naomi, ken)

    return decnaomi, warnaomi


def test():
    print solve([0.5], [0.6])
    print solve([7, 2], [8, 3])
    print solve([1, 5, 9], [3, 4, 6])
    naomi = '0.186 0.389 0.907 0.832 0.959 0.557 0.300 0.992 0.899'
    ken = '0.916 0.728 0.271 0.520 0.700 0.521 0.215 0.341 0.458'

    print solve(map(float, naomi.split()),
          map(float, ken.split()))

def main(fn):
    f = open(fn)
    T = int(f.next())
    for i in range(T):
        N = int(f.next())
        naomi = map(float, f.next().split())
        ken = map(float, f.next().split())
        a, b = solve(naomi, ken)
        print 'Case #%s: %s %s' % (i+1, a, b)


if __name__ == '__main__':
    #main('d_test.txt')
    main('D-large.in')
    #test()


