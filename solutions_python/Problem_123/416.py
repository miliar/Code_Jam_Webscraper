from math import ceil, log

t, T = 0, int(input())
while t!=T:
    t += 1

    A, N = tuple(map(int, input().split()))
    M = tuple(map(int, input().split()))

    M = sorted(M)
    ops = 0

    hist = [(ops,A,M[:])]
    while hist and hist[0][2]:
        ops,a,M = hist.pop(0)
      #  print(ops, a, M, 'got')
        while M and a>M[0]:
            a += M.pop(0)
   #     print(a, M)
        if M:
            m = M.pop(0)
    #        print(M, 'ch')
            hist.append((ops+1,a,M[:]))
     #       print(hist)
            if a > 1:
                n = int(ceil(log(m/(a-1),2)))
                ops += n
                a = (2**n)*(a-1)+1

                hist.append((ops,a+m,M[:]))
        else:
            hist.append((ops,0,False))
        hist.sort()
      #  print(hist)

    print("Case #%d:" % t, hist[0][0])
