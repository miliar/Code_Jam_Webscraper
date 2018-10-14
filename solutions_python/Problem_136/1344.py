import sys

inp = sys.stdin
get_int = lambda: int(inp.readline())
get_floats = lambda: map(float, inp.readline().split())

T = get_int()
for case_number in range(1, T + 1):
    C, F, X = get_floats()
    speed = 2
    time = 0
    while 1:
        nofarm = X / speed
        farm = C / speed
        withfarm = farm + (X / (speed + F))
        if withfarm < nofarm:
            time += farm
            speed += F
        else:
            time += nofarm
            break
    print 'Case #%d: %.7f' % (case_number, time)
