def BathroomStalls():
    N = raw_input().strip().split()

    result = 0 

    A = N[0]
    B = int(N[1])
    A = list(A)
    for i in xrange(len(A) - B+1):
        if A[i] == '-':
            for b in xrange(B):
                if A[i+b] == '-':
                    A[i+b] = '+'
                else:
                    A[i+b] = '-'
            result += 1
        # print A
    r = True
    for a in xrange(B):
        if A[len(A)-1-a] == '-':
            r = False
            break
    if r:
        result = str(result)
    else:
        result = "IMPOSSIBLE"
    return result

for case in xrange(input()):
    result = BathroomStalls()
    print 'Case #%d: %s' % (case+1,result)
