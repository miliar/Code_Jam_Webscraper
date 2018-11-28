#!/usr/bin/env python2


def time_to_buy_farms(c, f):
    t = 0.0
    rate = 2.0

    while True:
        yield t, rate

        t += (c/rate)
        rate += f


def min_time(c, f, x):
    current_min = None
    gen = time_to_buy_farms(c, f)

    while True:
        t, r = gen.next()
        total = t + (x / r)
        if current_min is None or total < current_min:
            current_min = total
        if total > current_min:
            return current_min


def main():
    outs = []

    with open('input.in', 'r') as inp:
        n_tests = int(inp.readline())

        for i in range(n_tests):
            c, f, x = map(float, inp.readline().split(' '))
            outs.append(
                'Case #{0}: {1:.7f}'.format(i+1, min_time(c, f, x))
            )

    with open('output.out', 'w') as out:
        out.write('\n'.join(outs))

if __name__ == '__main__':
    main()