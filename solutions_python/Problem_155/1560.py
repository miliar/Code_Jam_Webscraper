#!/usr/bin/env python3

import sys


def write_output_line(f, case, result):
    f.write('Case #{}: {}\n'.format(case, result))


def main(input_path, output_path):
    with open(input_path) as f_in, open(output_path, 'w') as f_out:
        f_in.readline()  # number of cases

        for n, line in enumerate(f_in):
            if not line.strip():
                continue

            num_standing = 0
            num_added = 0

            s_max, ss = line.split()
            s_max = int(s_max)
            ss = map(int, ss)

            for s, num_at_level in enumerate(ss):
                # precondition: this many people stand immediately
                # this is true for s=0 initially, then we make it true
                num_standing += num_at_level

                # if we have less standing than our next level, we need to
                # add a person (even if the next level is empty, as it will
                # never end in a 0)
                # we should always be able to add 1 at each level
                if num_standing < s  + 1:
                    num_added += 1
                    num_standing += 1

            write_output_line(f_out, n + 1, num_added)


if __name__ == '__main__':
    if not sys.argv[2:]:
        sys.argv.append(sys.argv[1].replace('in', 'out'))

    main(sys.argv[1], sys.argv[2])