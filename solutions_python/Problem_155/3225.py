total = int(raw_input())

for case in range(total):
    maxShy, config = raw_input().split()
    c = [int(count) for count in list(config)]

    h = 0
    curShy = c[0]

    for s in range(1, int(maxShy) + 1):
        if curShy >= s:
            curShy += c[s]
        else:
            addon = (s - curShy)
            h += addon
            curShy += (addon + c[s])

    print 'Case #%d: %d' % (case + 1, h)
