def steps(a, b):
    return abs(b - a) + 1

def process(line):
    parts = line.strip().split(' ')
    n = int(parts[0])
    opts = []
    for i in xrange(n):
        opts.append((parts[i*2+1], int(parts[i*2+2])))
    t = 1
    o = 1
    b = 1
    o_last = 0
    b_last = 0
    last = 0
    for opt in opts:
        bot, button = opt
        if bot == 'O':
            s = steps(o, button)
            o = button
            o_last = max(o_last + s, last + 1)
            last = o_last
        else:
            s = steps(b, button)
            b = button
            b_last = max(b_last + s, last + 1)
            last = b_last
    return last

with open('A-large.in', 'r') as f:
    line = f.readline()
    n = int(line)
    for i in xrange(n):
        line = f.readline()
        counts = process(line)
        print 'Case #%d: %d' % (i + 1, counts)
