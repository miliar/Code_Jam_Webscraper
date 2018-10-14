with open('in.txt','r') as f:
    f.readline()
    i = 0
    for line in f:
        i += 1

        s,n = line.split()
        n = int(n)
        s = list(s)
        m = len(s)
        ans = 0
        for j in range(m-n+1):
            if s[j] == '-': #flip
                if j + n > m:
                    ans = "IMPOSSIBLE"
                    break
                else:
                    ans += 1
                    for k in range(j,j+n):
                        s[k] = '-' if s[k] == '+' else '+'
        if '-' in s:
            ans = "IMPOSSIBLE"
        
        print "Case #%d: %s" % (i, ans)
