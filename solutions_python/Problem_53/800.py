#-*- coding: utf-8 -*-

T = int(raw_input())

for case in range(1, T+1):
    N, K = raw_input().split()
    N, K = int(N), int(K)

    for i in range(1, N+1):
        S =  K / (2**(i-1))
        if S%2 == 0:
            print "Case #%s: %s"%(case, 'OFF')
            break
    else:
        print "Case #%s: %s"%(case, 'ON')
