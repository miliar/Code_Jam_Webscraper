#!/usr/bin/python


n_tests = int(raw_input())

for test in range(n_tests):
    n,k = raw_input().split()
    n = int(n)
    k = int(k)

    bho = [1]
    bho += [0 for i in range(n)]
    bho += [1]

    ll = 0
    lr = n+1
    lastp = -1
    for p in range(k):
        bho[(ll+lr)/2] = 1
        lastp = (ll+lr)/2
        cll = ll = 0
        clr = lr = 0

        for i in range(n+2):

            if bho[i] == 1:
                clr = i
                if clr-cll > lr-ll:
                    ll = cll
                    lr = clr

                clr = cll = i
    

    a = 0
    b = 0
    for i in range(lastp-1,-1,-1):
        if bho[i] == 1:
            break
        a += 1

    for i in range(lastp+1,len(bho)):
        if bho[i] == 1:
            break
        b += 1
                
    print ("Case #"+str(test+1)+":"), max(a,b), min(a,b)

