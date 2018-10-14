#!/usr/bin/env python


inFile = open('in.txt', 'r')
outFile = open('out.txt', 'w')
t = int(inFile.readline())
for test in range(1, t+1):
    N, K = map(int, inFile.readline().split(' '))
    U = float(inFile.readline())
    probs = map(float, inFile.readline().split(' '))
    probs.sort()
    carry = 0
    prev = 0.0
    ans = 1
    cont = True
    for i in range(N):
        present = probs[i]
        if(cont):
            diff = (present - prev)*carry
            if(diff <= U):
                U -= diff
                prev = present
                carry += 1
            else:
                split = 0.0
                if(carry != 0):
                    split = U/carry
                prev += split
                ans = prev**carry
                ans *= present
                cont = False
        else:
            ans *= present
    # print prev, carry
    # print U

    if(cont):
        if(U != 0):
            split = 0.0
            if(carry != 0):
                split = U/carry
            prev += split
        ans = prev**carry
    outFile.write("Case #{}: {}\n".format(test, min(1.0000, ans)))
