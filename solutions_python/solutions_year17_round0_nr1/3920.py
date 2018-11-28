import itertools
import sys


def _get_flips(line):
    start_row, flipper = line.split()

    start_row = [i == '+' for i in start_row]
    flipper = int(flipper)

    branches = [start_row]
    dup = set()

    for flips in itertools.count():
        next_branches = []

        if len(branches) <= 0:
            return 'IMPOSSIBLE'

        for row in branches:
            if False not in row:
                return flips

            for i in range(0, len(row) - flipper + 1):
                cp = row[:]

                for j in range(i, i + flipper):
                    cp[j] = not cp[j]

                s = ''.join([str(int(i)) for i in cp])

                if s not in dup:
                    dup.add(s)
                    next_branches.append(cp)

        branches = next_branches


with open(sys.argv[1]) as f_in:
    with open(sys.argv[2], 'wt') as f_out:
        next(f_in)

        for i, line in enumerate(f_in):
            best = _get_flips(line)

            f_out.write('Case #{}: {res}\n'.format(i + 1, res=best))
            print('Case #{}: {res}'.format(i + 1, res=best))


print('~FIN~')
