T = input()

for case in range(T):
    N = input()
    C = [int(x) for x in raw_input().split()]
    psum = [False] * 20
    sum = 0
    min = C[0]

    for c in C:
        sum += c
        if c < min:
            min = c

        i = 0
        while c > 0:
            if c%2 == 1:
                psum[i] = not psum[i]
            i+=1
            c/=2

    f = reduce((lambda x,y: x or y), psum)
    if f: print "Case #%i: NO" % (case + 1)
    else: print "Case #%i: %i" % (case + 1, sum - min)
