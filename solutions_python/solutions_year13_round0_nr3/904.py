import itertools

def gen(d):
    l = [1, 4, 9, 121, 484]
    
    # welcome to debugging hell
    
    # Edge 1 (sum: 2)
    for length in range(3, d+1):
        if length % 2:
            for mid in [0, 1, 2]:
                if mid == 2: # perm cannot contain 2 (sum: 6)
                    for perm in filter(lambda x: sum(x) <= 1, itertools.product([0, 1], repeat=(length-3)/2)):
                        sp = sum([n*(10**i) for i, n in enumerate([1] + list(perm) + [2] + list(perm)[::-1] + [1])]) ** 2
                        l += [sp]
                else:
                    for perm in filter(lambda x: sum(x) <= 3, itertools.product([0, 1], repeat=(length-3)/2)):
                        sp = sum([n*(10**i) for i, n in enumerate([1] + list(perm) + [mid] + list(perm)[::-1] + [1])]) ** 2
                        l += [sp]
        else:
            for perm in filter(lambda x: sum(x) <= 3, itertools.product([0, 1], repeat=(length-2)/2)):
                sp = sum([n*(10**i) for i, n in enumerate([1] + list(perm) + list(perm)[::-1] + [1])]) ** 2
                l += [sp]
    # Edge 2 (sum: 8)
    for length in range(3, d+1):
        if length % 2:
            for mid in [0, 1]: # perm can only contain zeros
                perm = [0] * ((length-3)/2)
                sp = sum([n*(10**i) for i, n in enumerate([2] + list(perm) + [mid] + list(perm)[::-1] + [2])]) ** 2
                l += [sp]
        else:
            sp = sum([n*(10**i) for i, n in enumerate([2] + [0] * (length-2) + [2])]) ** 2
            l += [sp]
    return l

l = gen(50)
for TC in range(1, input()+1):
    a, b = map(int, raw_input().split())
    print 'Case #%d: %d' % (TC, len(filter(lambda x: a <= x <= b, l)))