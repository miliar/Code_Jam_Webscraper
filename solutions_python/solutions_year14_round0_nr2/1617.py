def yend(fn):
    if fn == 0:
        return x/2
    fn -= 1
    y = 0
    for i in range(0, fn+1):
        y += c/(2 + i*f)
    fn += 1
    y += x/(2+fn*f)
    return y

t = int(input())
for tc in range(1, t+1):
    (c, f, x) = [float(i) for i in input().split()]
    yenew = yend(0)
    for i in range(1, 10**10):
        yeold = yenew
        yenew = yend(i)
        if yenew > yeold:
            break
    print('Case #%i: %.7f' % (tc, yeold))



#ziel: x cookies übrig haben
#ausgangsrate 2, pro farm f extra
#farmpreis c


#cookieentwicklung ohne farm:
#   2, 4, 6, ...    ->  y*2

#mit einer farm:
#   2+f, 4+2f, 8+4f, ...    ->  y*(2+f)

#generell mit konst farmzahl:
#   y*(2 + fn*f)

#-> yend generell mit konst fzahl:
#   yend = x/(2 + fn*f)

#-> yend gesamt bis alle farmen:
#   c/2 + c/(2+f) + c/(2+2*f) + c/(2+3*f) + ...

#dazu:
#   x/(2+fn*f)
