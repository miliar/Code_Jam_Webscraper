def numagain(n):
    sum = 0
    mult = 1
    i = len(n)-1
    while i >= 0:
        sum += n[i] * mult
        mult *= 10
        i -= 1
    return sum

def g(n):
    if len(n) == 1:
        return numagain(n)

    prev = 0
    for i in xrange(len(n)):
        curr = n[i]
        if prev > curr:
            n[i-1] = prev-1
            for fill in xrange(i, len(n)):
                n[fill] = 9

            if n[i-2] > n[i-1]:
                fill = i-1
                while n[fill-1] >= n[fill] and fill != 0:
                    n[fill] = 9
                    fill -= 1
                if i > 1:
                    n[fill] -= 1
            return numagain(n)
        prev = curr
    return numagain(n)

def f(n):
    nlist = [int(numchar) for numchar in str(n)]
    return g(nlist)




t = int(raw_input())
for i in xrange(1, t+1):
    n = int(raw_input())
    print 'Case #{}: {}'.format(i, f(n))
