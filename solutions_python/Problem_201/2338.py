import math


def minMax(n, k, o):
    if k == 1:
        o.write(str(math.floor(n/2)) + ' ' + str(math.ceil(n/2) - 1) + '\n')
    else:
        if k % 2:
            minMax(math.ceil(n / 2) - 1, (k - 1) / 2, o)
        else:
            minMax(math.floor(n / 2), k / 2, o)


i = open('C-small-2-attempt0.in', 'r')
o = open('solution.out', 'w')
it = 0
for line in i:
    if it:
        o.write('Case #' + str(it) + ': ')
        n, k = [int(x) for x in line.split()]
        minMax(n, k, o)
    it += 1
