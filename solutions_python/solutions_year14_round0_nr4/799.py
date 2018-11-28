def readint():
    return int(raw_input())
def readfloat():
    return float(raw_input())
def readarray(N, foo=raw_input):
    return [foo() for i in xrange(N)]
def readlinearray(foo=int):
    return map(foo, raw_input().split())


case_number = readint()
for case in xrange(case_number):
    N = readint()
    na = readlinearray(float)
    ke = readlinearray(float)
    na.sort()
    ke.sort()
    
    fair = 0
    n = 0
    k = 0
    while k < N:
        if na[n] < ke[k]:
            fair += 1
            n += 1
        k += 1

    lie = 0
    n = 0
    k = 0
    while n < N:
        if na[n] > ke[k]:
            lie += 1
            k += 1
        n += 1

    print "Case #%s: %d %d" % (case + 1, lie, N - fair)
