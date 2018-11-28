T = int(raw_input())

def foo(X, C, F):
    speed = 2.
    t = 0.
    while True:
        dt = C / speed
        cross = speed**2 * 1. / F * dt + speed * dt
        if cross >= X:
            return t + X / speed
        t += dt
        speed += F

for i in range(T):
    C, F, X = [float(x) for x in raw_input().split()]
    print 'Case #%d: %.7f' % (i+1, foo(X, C, F))
