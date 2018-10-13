#Joe Snider
#4/16
#
#code jam 2017, qual B

#tidy the number (first non-decreasing <= the input)
def tidy(n):
    s = []
    for x in str(n):
        s.append(x)
    for i in range(len(s)-1, 0, -1):
        l = int(s[i])
        k = int(s[i-1])
        if l < k:
            for j in range(i, len(s)):
                s[j] = '9'
            s[i-1] = str(k-1)
    return int("".join(s))

#raw_imput is one line    
t = int(raw_input())
for i in xrange(1, t + 1):
    n = int(raw_input())
    print "Case #%d: %d"%(i, tidy(n))
