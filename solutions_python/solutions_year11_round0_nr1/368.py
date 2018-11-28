def case():
    line = raw_input().split()
    buttons = zip(line[1::2], map(int, line[2::2]))
    pos = {'O': 1, 'B': 1}
    saved = {'O': 0, 'B': 0}
    other = {'O': 'B', 'B': 'O'}
    time = 0
    for i, (bot, button) in enumerate(buttons):
        dt = abs(button-pos[bot])-saved[bot]
        dt = max(0, dt)
        dt += 1
        print bot, 'has to walk', abs(button-pos[bot])
        print bot, 'has saved', saved[bot]
        print 'saving', dt, 'for', other[bot]
        saved[bot] = 0
        saved[other[bot]] += dt
        time += dt
        pos[bot] = button
        print 'time taken:', time
        print
    return time

T = int(raw_input())
for i in xrange(1, T+1):
    print 'Case #%i: %i' % (i, case())
