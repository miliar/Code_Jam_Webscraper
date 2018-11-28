t = int(raw_input())
for i in range(t):
    s, n = raw_input().split()
    s = list(s)
    n = int(n)
    res = 0
    for x in range(len(s)-n+1):
        if "-" == s[x:x+n][0]:
            res += 1
            for y in range(x, x+n):
                if s[y] == "+":
                    s[y] = "-"
                else:
                    s[y] = "+"
    print "Case #" + str(i+1) + ":", 
    if len(set(s)) == 1:
        print res
    else:
        print "IMPOSSIBLE"
