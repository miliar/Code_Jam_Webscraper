for t in xrange(1, input()+1):
    n = input()
    j = str(n)
    print "Case #" + str(t) + ":",
    if len(j) < 2:
        print n
    else:
        A = [int(i) for i in j]
        equ = []
        start, end = 0, len(j)-1
        if sum(A) == 1:
            print ''.join(str('9') for i in range(end))
        else:
            while start < end:
                if A[start] > A[start+1]:
                    A[start] -= 1
                    A[start+1:] = [9] * (len(A) - start - 1)
                elif A[start] == A[start+1]:
                    if A[start] > A[end]:
                        A[start] -= 1
                        A[start+1:] = [9] * (len(A) - start - 1)
                start += 1

            if A[0] == 0:
                del A[0]

            print ''.join(str(i) for i in A)
