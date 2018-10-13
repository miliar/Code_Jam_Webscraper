cases = int(raw_input())
for i in xrange(1, cases + 1):
    c, f, x = [float(x) for x in raw_input().split()]
    total = 0.0
    cookies = 2
    time = 0.0
    while True:
        required = x / cookies
        other = c / cookies + x / (cookies + f)
        if required <= other:
            time += required
            break
        time += c / cookies
        cookies += f

    print 'Case #%d: %.7f' % (i, time,)
