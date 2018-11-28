#!/usr/bin/python
T = int(raw_input())
for i in range(T+1)[1:]:
    ans = raw_input()
    N = list(ans)
    L = len(ans)
    j = 0
    start = 0
    #print ans
    while j != L - 1:
        if N[j] < N[j + 1]:
            start = j+1
        elif N[j] > N[j+1]:
            #print "start",start,"j", j, "L",L
            n = []
            for k in range(L - j - 1):
                n.append("9")
            n = "".join(n)
            m = []
            m.append(str(int(ans[start]) - 1))
            for k in range(j - start):
                m.append("9")
            m = "".join(m)
            ans = ans[0:start] +m+n
            break
        j += 1
    ans = int(ans)
    print "Case #"+str(i)+": "+str(ans)
