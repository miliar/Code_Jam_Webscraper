

f = open(r"e:\downloads\B-large.in", "r")
#f = open(r"e:\downloads\cookie_clicker_alpha.txt", "r")

T = int(f.readline())
for t in range(1, T+1):
    C, F, X = map(float, f.readline().split())
    res, rate, cookies = 0.0, 2, 0 # time & cookies
    while True:
        t1 = (C-cookies)/rate + X/(rate+F)
        t2 = (X-cookies)/rate
        if t1 <= t2:
            res += (C-cookies)/rate
            rate += F
            cookies = 0.0
        else:
            res += t2

            break


    print("Case #%d: %s" % (t, repr(res)))