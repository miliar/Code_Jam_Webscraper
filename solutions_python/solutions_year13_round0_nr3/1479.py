f = open('C-small-attempt0.in')
r = open('out.txt', 'w')

import math
def is_fair_and_square(n):
    return str(n) == str(n)[::-1] and str(n**2) == str(n**2)[::-1]

n = int(f.readline().strip())
for i in range(n):
    low, hi = [int(x) for x in f.readline().strip().split()]
    count = 0
    for j in range(int(math.ceil(math.sqrt(low))), int(math.sqrt(hi))+1):
        if is_fair_and_square(j):
            count += 1
    r.write('Case #' + str(i+1) + ': ' + str(count) + '\n')

f.close()
r.close()
