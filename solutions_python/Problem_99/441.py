from operator import mul

f = open('/Users/Mac/Dropbox/Code Jam/2012/1A/A/In.in')

numcases = int(f.readline())


    
for a in range(numcases):
    print "Case #%d:" % (a+1),
    z, n = map(int,f.readline().split())
    k = n-z

    l = map(float, f.readline().split())

    pAll = reduce(mul, l)
    pNAll = 1 - pAll

    one = (pAll*(k+1)) + (pNAll * (n + k + 2)) #P(all) + P(notall)
    
    two = 1000000000.0
    if z > 1:
        for b in range(z-1):
            b = b+1
            p1 = reduce(mul, l[:-b]) #P(first n-i are correct)
            p1 = p1 * (2*b + (k + 1)) + ( (1-p1) * (2 * b + k+1 + n+1) )
            if p1 < two:
                two = p1


    three = 2 + n

    one = round(one, 6)
    two = round(two, 6)
    three = round(three, 6)
    print '%.6f' % min(one, two, three)
    if k == 0:
        print "FUFCK"
    
