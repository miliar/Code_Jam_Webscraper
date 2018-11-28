def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a - b * (a / b))

with open('B-small-attempt1.in') as infile:
    length = int(infile.readline())
    for i in xrange(1, length + 1):
        line = infile.readline().strip()
        if not line.strip(): continue
        data = line.split()[1:]
        data = [int(d) for d in data]
        diff1 = abs(data[1] - data[0])     
        if len(data) > 2:
            diff2 = abs(data[2] - data[0])
            diff3 = abs(data[2] - data[1])
            x = gcd(diff1, diff2)
        else:
            x = diff1
        print 'Case #%s: %s' % (i, abs(data[0] % -x))
