import sys
T = int(raw_input())
for t in range(T):
    _, s = raw_input().split()
    n = 0
    res = 0
    s = list(s)
    for i in range(len(s)):
        if n < i + 1:
            res += (i-n)
            n += (i-n)
        n += int(s[i])
    print "Case #" +  str(t+1) +  ": " + str(res) 


    