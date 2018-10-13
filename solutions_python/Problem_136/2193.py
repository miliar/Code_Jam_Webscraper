#!/usr/bin/python3

def calc_time(c, f, x):
    def buy_farm_or_not(c,f,x,cookie,v,mt,tt):
        co = cookie
        vv = v
        co -= c
        vv += f
        TT = tt + (x - co) / vv
        if TT < mt:
            return (co,vv,TT)
        else:
            return (cookie,v,mt)

    def time_fast_forward(c,v,x,cookie,tt):
        if x - cookie >= c:
            ct = c / v
            return(cookie+c,tt+ct)
        else:
            return(x,tt+(x-cookie)/v)

    mt = x / 2
    tt = 0
    v = 2
    cookie = 0

    if c >= x:
        return x / v

    while cookie < x:
        cookie, tt = time_fast_forward(c,v,x,cookie,tt)
        cookie, v, mt = buy_farm_or_not(c,f,x,cookie,v,mt,tt)
        #print(cookie,v,tt,mt)

    return tt

tol = int(input())

for l in range(1, tol+1):
    ln = [float(item) for item in input().split(' ')]
    tt = calc_time(*ln)
    print('Case #%d: %.9f' % (l, tt))
