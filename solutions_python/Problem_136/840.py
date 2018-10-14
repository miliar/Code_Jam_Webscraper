from sys import stdin

def ttf_no_farm(X, c, rate):
    return (X - c)/float(rate)

def ttf_farm(C, F, X, c, rate):
    t = 0

    if c >= C:
        c -= C
    else:
        t += ttf_no_farm(C, c, rate)
        c = 0

    t += (X - c)/(rate + F)

    return t

T = int(stdin.readline())

for k in xrange(T):
    C, F, X = map(float, stdin.readline().split())

    rate = 2
    time = 0
    cookies = 0

    while cookies < X:
        no_farm = ttf_no_farm(X, cookies, rate)
        farm = ttf_farm(C, F, X, cookies, rate)

        if no_farm <= farm:
            time += no_farm
            cookies = X
            break
        else:
            if C < cookies:
                cookies -= C
            else:
                time += ttf_no_farm(C, cookies, rate)
                cookies = 0

            rate += F

    print 'Case #%d: %.7f' % (k+1, time)
