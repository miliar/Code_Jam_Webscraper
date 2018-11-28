def gcd(x, y):
    if y == 0:
        return x
    if x < y:
        return gcd(y, x)
    return gcd(y, x%y)

def solve_jamcode():
    line = raw_input()
    line = line.split()
    T = int(line[0])
    for t in xrange(1, T+1):
        line = raw_input()
        line = line.split()
        N = int(line[0])
        events = [int(e) for e in line[1:]]
        events.sort()
        diffs = []
        for n in xrange(N-1):
            diffs.append(events[n+1] - events[n])
        g = reduce(gcd, diffs)
        if events[0] % g == 0:
            a = events[0] / g
        else:
            a = (events[0] // g) + 1
        a = a * g - events[0]
        '''print 'gcd: ', g'''
        print 'Case #' + str(t) + ':', a


if __name__ == '__main__':
    solve_jamcode()
