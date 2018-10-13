

cases = int(raw_input())

for case in range(1, cases+1):
    cps = 2.0
    cost, deltacps, target = map(float, raw_input().split())
    time = 0.0
    # Always buy a new farm when delta time incurred is less than target/cps
    # Crappy iterative solution for now
    while cost/cps + target/(cps+deltacps) < target/cps:
        time += cost/cps
        cps += deltacps
    time += target/cps
    print "Case #{0}: {1:.7f}".format(case, time)