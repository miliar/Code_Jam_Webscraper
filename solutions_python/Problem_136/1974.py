import fileinput


def speed_with_houses(h, F):
    return 2+h*F


def solve(C, F, X):
    previous = float('inf')
    c_buyed = 0
    while True:
        h_time = sum([(C/speed_with_houses(h, F)) for h in xrange(c_buyed)])
        x_time = X/speed_with_houses(c_buyed, F)
        time = h_time+x_time
        if time > previous:
            return previous
        previous = time
        c_buyed += 1


def run():
    f = fileinput.input()
    T = int(f.readline())
    for t in xrange(1, T + 1):
        C, F, X = [float(i) for i in f.readline().strip().split(' ')]
        time = solve(C, F, X)
        print 'Case #%d: %.7f' % (t, time)


if __name__ == '__main__':
    run()