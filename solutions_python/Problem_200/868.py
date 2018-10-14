#!/bin/python

T = int(raw_input().strip())

for c in range(1, T + 1):
    N = map(int, raw_input())
    #get the first out of order, then decrease by 1 and set the rest to 9s
    found = False
    while not found:
        found = True
        for i in range(len(N)-1):
            d1,d2 = N[i], N[i+1]
            if d1 > d2:
                N[i] = 9 if d1 == 0 else d1-1
                for j in range(i+1, len(N)): N[j] = 9
                found = False
                break

    #strip leading 0s
    ind = 0
    while N[ind] == 0: ind += 1
    ans = ''.join(map(str, N[ind:]))
    print 'Case #' + str(c) + ': ' + ans
