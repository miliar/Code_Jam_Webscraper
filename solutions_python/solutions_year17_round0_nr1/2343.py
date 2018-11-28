def solve(s, k):
    a=[]
    for i in xrange(0, len(s)):
        a.append(0)
    ans = 0
    for i in xrange(0, len(s)-k+1):
        if (s[i] == '-' and a[i] % 2 == 0) or (s[i] == '+' and a[i] % 2 == 1):
            for j in xrange(i,i+k):
                a[j] += 1
            #print "flip at "+str(i)
            ans += 1
    for i in xrange(len(s)-k+1, len(s)):
        if (s[i] == '-' and a[i] % 2 == 0) or (s[i] == '+' and a[i] % 2 == 1):
            return "IMPOSSIBLE"
    return ans

t=int(raw_input())
for cas in xrange(1, t + 1):
    s, k = raw_input().split()
    k = int(k)
    print "Case #{}: {}".format(cas, solve(s,k))
