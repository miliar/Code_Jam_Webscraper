def solve(a):
    req = 0
    count = 0
    for i in xrange(len(a)):
        if count >= i:
            count += int(a[i])
        else:
            n = i-count
            count += n+int(a[i])
            req += n
    return req

for _ in xrange(input()):
    a = raw_input().split()[1]
    print "Case #%d:"%(_+1), solve(a)