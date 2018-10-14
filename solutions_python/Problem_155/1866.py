#!/usr/bin/python2

T = int(raw_input().split()[0])

for case in range(T):
    [sMax, sString] = raw_input().split()
    sMax = int(sMax)

    standing = 0
    shills   = 0
    for i in range(len(sString)):
        if standing < i:
            shills   += 1
            standing += 1
        standing += int(sString[i])

    print 'Case #' + str(case + 1) + ': ' + str(shills)
