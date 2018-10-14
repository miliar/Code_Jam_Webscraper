import math

cache = {}

def solve3(n, k):
    global cache
    if (n, k) in cache:
        return cache[(n, k)]
    if k == 1:
        cache[(n, k)] = (math.ceil((n - 1)/2.0), math.floor((n - 1)/2.0))
    elif k == 2:
        cache[(n,k)] = solve3(math.floor(n / 2), k - 1)
    else:
#         print('min(solve(%d, %d), solve(%d, %d))' % (math.ceil((n - 1) / 2), math.ceil((k - 1) / 2),
#                                                     math.floor((n - 1)/ 2), math.floor((k - 1) / 2)))
        cache[(n,k)] = min([solve3(math.ceil((n - 1) / 2), math.ceil((k - 1) / 2)),
                            solve3(math.floor((n - 1)/ 2), math.floor((k - 1) / 2))
                           ])
    return cache[(n, k)]

with open('out3', 'wt') as o:
    for i, line in enumerate([l.strip() for l in open('C-small-1-attempt1.in').readlines()[1:]], 1):
        print('\nsolving:', line)
        n, k = [int(i) for i in line.split()]
        a, b = solve3(n, k)
        result = 'Case #%d: %d %d' % (i, a, b)
        print(result)
        _ = o.write(result + '\n')

