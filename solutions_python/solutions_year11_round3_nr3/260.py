#!/usr/bin/python
#gcj 2011 roundC pc small
T = int (input())
for cases in range(T):
    s = raw_input().split(' ')
    n = int(s[0])
    l = int(s[1])
    p = int(s[2])

    s = raw_input().split(' ')
    ans = 'NO'
    for i in range(l,p+1):
        done = 1
        for j in s:
            k=int(j)
            if k%i == 0 or i%k == 0:
                pass
            else:
                done = 0
        if done:
            ans = str(i)
            break

    print 'Case #'+str(cases+1)+': '+ ans


