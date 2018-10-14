cts = input()
for ct in range(1, cts + 1):
    time = 0.0
    cookierate = 2.0
    c, f, x = [float(entry) for entry in raw_input().split()]

    perfect = x/cookierate
    while perfect >= (time + c/cookierate + x/(cookierate + f)):
        time += c/cookierate
        cookierate += f
        perfect = time + x/cookierate
        #print "Perfect: %f, %f, %f" % (perfect, time, time + c/cookierate + x/(cookierate + f))

    print "Case #%d: %.7f" % (ct, perfect)
