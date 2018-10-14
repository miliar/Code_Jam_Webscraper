import sys

def cookie(c, f, x):
    time = 0.0
    rate = 2.0

    if x <= c:
        return x / rate

    x_left = x - c

    while True:
        new_rate = rate + f

        t_left_cur = x_left / rate
        t_left_new = x / new_rate

        if t_left_new < t_left_cur:
            time += c / rate
            rate += f
        else:
            return time + x / rate

def main():
    with open(sys.argv[1]) as f:
        lines = [l.rstrip() for l in f.readlines()[1:]]

    for i, params in enumerate(lines, 1):
        c, f, x = map(float, params.split())

        y = cookie(c, f, x)
        print 'Case #{0}: {1:.7f}'.format(i, y)

if __name__ == '__main__':
    main()
