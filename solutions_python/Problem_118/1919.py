def pal(x):
    x = str(x)
    return x == x[::-1]

pals = [1,4,9]

for i in range(11, 1000):
    if not pal(i):
        continue
    ii = i*i
    if pal(ii):
        pals.append(ii)

import bisect
for case in range(1, input()+1):
    a,b = map(int, raw_input().split())
    print 'Case #{}: {}'.format(
        case,
        bisect.bisect_right(pals, b) - bisect.bisect_left(pals, a)
    )
    
