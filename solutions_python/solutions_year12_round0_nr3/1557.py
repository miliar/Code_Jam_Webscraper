f = open('c.in')
n = int(f.readline())

for testcase in range(1, n + 1):
    a, b = map(int, f.readline().split())
    count = 0
    strb = str(b)
    for i in range(a, b):
        stri = str(i)
        for l in range(1, len(stri)):
            t = int(stri[l:] + stri[:l])
            if i < t and t <= b:
                #print stri, t
                count += 1
                assert a <= i and i < t and t <= b
    print 'Case #%d: %d' % (testcase, count)
