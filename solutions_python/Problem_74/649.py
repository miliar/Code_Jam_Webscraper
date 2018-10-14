numTests = input()
for case in range(1, numTests + 1):
    values = raw_input().split()
    totalSwitches = int(values[0])
    ops = zip(values[1::2], map(int, values[2::2]))
    t = 0
    o = 1
    b = 1
    lastBot = 'n'
    elapsed = 0
    for bot, target in ops:
        curPos = o if bot == 'O' else b
        delta = abs(curPos - target) + 1
        if lastBot == bot:
            t += delta
            elapsed += delta
        else:
            if elapsed >= delta:
                t += 1
                elapsed = 1
            else:
                t += delta - elapsed
                elapsed = delta - elapsed
        lastBot = bot
        if bot == 'O':
            o = target
        else:
            b = target

    print "Case #%d: %d" % (case, t)
