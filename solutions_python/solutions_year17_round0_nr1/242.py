#!/usr/bin/python
T = int(raw_input())
for i in range(T+1)[1:]:
    ans = 0
    l = raw_input()
    ar, k = l.split()
    a = []
    for j in ar:
        a.append(j)
    k = int(k)
    j = 0
    while j <= len(a) - k:
        if a[j] == '-':
            ans += 1
            for itr in range(k):
                if (a[j + itr] == "+"):
                    a[j + itr] = '-'
                else:
                    a[j + itr] = '+'
        j+=1
    while j < len(a):
        if a[j] == '-':
            ans = -1
            break
        j += 1
    if ans == -1:
        ans = "IMPOSSIBLE"
    else:
        ans = str(ans)
    print "Case #"+str(i)+": "+str(ans)
