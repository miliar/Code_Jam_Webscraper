f = open('A-large.in')

n = int(f.readline())
sd = dict()

for i in range(n):
    s = int(f.readline())
    sw = 0

    # create a dictionary of engines
    sd = dict()
    for j in range(s):
        sd[f.readline()] = 0
    swname = ''

    q = int(f.readline())
    for qq in range(q):
        se = f.readline()
        sd[se] = sd[se] + 1

        # time to switch
        if not 0 in sd.values():
            sw = sw + 1
            # maybe need to switch twice?
            if se == swname: sw = sw + 1
            swname = se
            # clear up dictionary
            for k in sd.keys():
                sd[k] = 0
            sd[se] = sd[se] + 1

    print 'Case #%d: %d' % (i+1, sw)
