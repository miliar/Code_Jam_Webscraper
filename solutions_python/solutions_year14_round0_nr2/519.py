t = input()

for case in range(1, t + 1):
    c, f, x = (float(x) for x in raw_input().split())
    cps = 2
    time = 0
    while (c/cps + x/(cps + f)) <= x/cps:
        time += c/cps
        cps += f
    print "Case #%d: %.7f" % (case, time + x/cps)
