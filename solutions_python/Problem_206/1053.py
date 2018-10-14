import sys



TEST = False
def dprint(*args):
    if TEST:
        print(*args)


if __name__ == '__main__':

    if sys.argv[1] == 'testy':
        # Add hand testy here
        pass

    f = open(sys.argv[1])

    cases = int(next(f))

    outf = open(sys.argv[1].replace('.in', '.out'), 'w')

    def print_output(i, *args):
        outf.write('Case #{}: {}'.format(i+1, ' '.join(str(x) for x in args)))
        outf.write('\n')

    # PROBLEM
    for case_i in range(cases):

        dprint(case_i)

        end, N = [int(i) for i in next(f).split(' ')]

        horses = [
            [int(i) for i in next(f).split(' ')]
            for _ in range(N)
        ]
        dprint(horses)

        times = [
            (end - start) / speed
            for start, speed in horses
        ]
        dprint(times)

        max_time = max(times)

        speed = end / max_time

        dprint(speed)
        print_output(case_i, speed)
