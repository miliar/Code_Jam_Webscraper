import sys

for cases in xrange(int(sys.stdin.readline())):
    n,s = sys.stdin.readline().strip().split()
    ans = 0
    curr = int(s[0])
    t = 1
    for i in s[1:]:
        if curr < t and int(i)!=0:
            ans += t-curr
            curr += t-curr
        curr += int(i)
        t += 1
    print "Case #%d: %d"%(cases+1,ans)
