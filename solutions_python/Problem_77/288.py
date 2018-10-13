c = int(raw_input())
for case in range(1, c+1):
    n = int(raw_input())
    a = map(int,raw_input().split())

    s = sorted(a)
    d = sum(1 for i in range(len(s)) if s[i]!=a[i])

    

    print "Case #%d: %6f" % (case, d)
