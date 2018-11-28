n = raw_input("")
n = int(n)

ans = []

for i in range(n):
    s = raw_input("")
    d = '1' * len(s)
    if (s < d):
        ans.append('9'*(len(s)-1))
    else:
        s = list(s)

        t = True
        for i in range(len(s)-1):
            if s[i] > s[i+1]:
                t = False
                break

        if t:
            ans.append("".join(s))
            continue
        
        e = list('9' * len(s))
        for i in range(len(s)-1):
            if s[i] <= s[i+1]:
                e[i] = s[i]
            else:
                e[i] = str(int(s[i])-1)
                break
        e = "".join(e)
        ans.append(e)

for i in range(n):
    print "Case #" + str(i+1) + ": " + str(ans[i])
