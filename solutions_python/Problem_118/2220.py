import itertools
digits = 4
for k in range(2, digits):
    palin = [sum([n*(10**i) for i,n in enumerate(([x]+list(ys)+[z]+list(ys)[::-1]+[x]) if k%2
                                    else ([x]+list(ys)+list(ys)[::-1]+[x]))])
                for x in range(1,10)
                                for ys in itertools.permutations(range(10), k/2-1)
                                                for z in (range(10) if k%2 else (None,))]

square_palin = [1, 4, 9, 121, 484]
for num in palin:
    sqr = num*num
    if str(sqr) == str(sqr)[::-1]:
        square_palin +=[sqr]
T = int(raw_input())
for i in range(T):
    a, b = [int(x) for x in raw_input().split()]
    count = 0
    
    for num in square_palin:
        if num >= a and num <=b:
            count += 1
    print 'Case #%d: %d' %(i+1, count)

