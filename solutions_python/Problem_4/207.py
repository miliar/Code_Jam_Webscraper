def next_perm(a):
    k = len(a) - 1
    while k > 0 and a[k-1] >= a[k]:
        k = k - 1

    if k == 0:
        return False

    k = k - 1

    j = len(a) - 1
    while a[j] <= a[k]:
        j = j - 1

    a[j], a[k] = a[k], a[j]

    reverse(a,k+1)

    return True


def reverse(a,k):
    n = len(a) - 1
    while k < n:
        a[k], a[n] = a[n], a[k]
        k = k + 1
        n = n - 1


def dotprod(v1,v2):
    d = 0
    for k in range(len(v1)):
        d += v1[k]*v2[k]
    return d


def main():
##    f = open('A-test.in', 'r')
    f = open('A-small-attempt0.in', 'r')

    N_cases = int(f.readline().split()[0])

    for case in range(N_cases):
        N = int(f.readline().split()[0])

        aux = f.readline().split()
        v1 = [int(x) for x in aux]

        aux = f.readline().split()
        v2 = [int(x) for x in aux]

        perm = range(N)

        perm_v2 = [v2[x] for x in perm]
        min_prod = dotprod(v1, perm_v2)

        while next_perm(perm):
            perm_v2 = [v2[x] for x in perm]
            prod = dotprod(v1, perm_v2)
            if prod < min_prod:
                min_prod = prod

        print 'Case #%d: %d' % ((case + 1), min_prod)


    f.close()

main()