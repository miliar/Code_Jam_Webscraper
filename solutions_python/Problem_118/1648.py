def fair(n):
    s = str(n)
    return s == s[::-1]


def generate(n):
    result = []
    for n in xrange(1, n + 1):
        if fair(n) and fair(n * n):
            result.append(n * n)
    return result


candidates = generate(10**7)
cases = input()
for test in xrange(1, cases + 1):
    a, b = [eval(x) for x in raw_input().split(' ')]
    result = sum([x >= a and x <= b for x in candidates])
    print 'Case #{}: {}'.format(test, result)
