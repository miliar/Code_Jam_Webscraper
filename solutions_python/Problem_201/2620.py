import math
f = open('stalls.in', 'r')
out = open('stalls.out', 'w')
f.readline()

test_case = 1
# brute force
for l in f:
    N = int(l.split(' ')[0])
    K = int(l.split(' ')[1])
    spaces = [N]
    for i in range(K - 1):
        # Find max
        mn = max(spaces)
        spaces += [int(math.ceil((mn - 1) / 2.0)),
                   int(math.floor((mn - 1) / 2.0))]
        spaces.remove(mn)
    mn = max(spaces)
    l, r = (int(math.ceil((mn - 1.0) / 2)), int(math.floor((mn - 1) / 2.0)))
    out.write('Case #{}: {} {}\n'.format(test_case, l, r))
    test_case += 1

'''
for l in f:
    N = int(l.split(' ')[0])
    K = int(l.split(' ')[1])
    layers = K.bit_length()
    factor = 1
    while True:
        if N % 2 == 0:
            if bin(K)[i + 1]:
                N = N / 2 - 1
            else:
                N = N / 2
        else:
            N = (N - 1) / 2
            factor = factor * 2
'''
