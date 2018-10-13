import math
countTrials = int(input())
for a in range(countTrials):
    data = input().split(' ')
    n = int(data[0])
    k = int(data[1])
    i = int(math.log(k,2))
    series = 2 ** i
    mult = 2 * series
    base = int(n / mult)
    left = n % mult + 1
    j = k - int(mult / 2) + 1
    if(j <= left):
        ls = base
    else:
        ls = base - 1
    if((j + series) <= left):
        rs = base
    else:
        rs = base - 1
    print('Case #%i: %i %i' % (a + 1, ls, rs))