from functools import reduce

t = int(input())

for cas in range(1, t+1):
    digits = [int(c) for c in input()]
    n = len(digits)
    for i in range(30):
        try:
            cliff = next(i-1 for i in range(1, n) if digits[i] < digits[i-1])
            digits = digits[:cliff] + [digits[cliff]-1] + [9]*(n-cliff-1)
        except:
            pass
    onum = reduce(lambda x,a: 10*x+a, digits)
    print('Case #{}: {}'.format(cas, onum))



