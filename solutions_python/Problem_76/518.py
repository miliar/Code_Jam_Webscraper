def split(line):
    parts = line.strip().split(' ')
    numbers = [int(k) for k in parts]
    result = reduce(lambda x, y: x^y, numbers)
    if result != 0:
        return -1
    else:
        return sum(numbers) - min(numbers)

with open('C-large.in', 'r') as f:
    line = f.readline()
    t = int(line)
    for i in range(t):
        line = f.readline()
        line = f.readline()
        m = split(line)
        if m > 0:
            print 'Case #%d: %d' % (i + 1, m)
        else:
            print 'Case #%d: NO' % (i + 1)
