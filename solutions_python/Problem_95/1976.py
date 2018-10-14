f = open("in")
T = int(f.readline())

start = ['ejp mysljylc kd kxveddknmc re jsicpdrysi','rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd','de kr kd eoya kw aej tysr re ujdr lkgc jv','a','o','z']
end = ['our language is impossible to understand','there are twenty six factorial possibilities','so it is okay if you want to just give up','y','e','q']

def charFrom(c):
    a = ' '.join(start)
    b = ' '.join(end)
    for i in range(len(a)):
        if c == a[i]:
            return b[i]
    return 'z'

for testcase in xrange(T):
    case = testcase+1

    line = f.readline().strip()
    ans = ''
    for c in line:
        ans += charFrom(c)

    print "Case #%d: %s" % (case, ans)
