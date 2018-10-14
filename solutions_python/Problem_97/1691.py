
def solve(data):
    data    = data.split(' ')
    min = int(data[0])
    max = int(data[1])

    if min < 10:
        return 0

    was = []
    count   = 0
    for i in xrange(min, max):
        t   = str(i)
        for j in xrange(1, len(t)):
            tmp = int(t[-j:len(t)] + t[0:-j])
            if tmp < min or tmp == i:
                continue
            if tmp <= max and [tmp, i] not in was and [i,tmp] not in was:
                was.append([tmp, i])
                was.append([i, tmp])
                count   = count + 1

    return count


if __name__ == '__main__':
    import sys
    T   = int(sys.stdin.readline())
    for i in xrange(T):
        data    = sys.stdin.readline().strip()
        out = solve(data)
        print "Case #%s: %s" % (i+1, out)
