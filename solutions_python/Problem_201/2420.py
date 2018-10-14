#!/usr/bin/env python3

"""Problem

A certain bathroom has N + 2 stalls in a single row; the stalls on the
left and right ends are permanently occupied by the bathroom
guards. The other N stalls are for users.

Whenever someone enters the bathroom, they try to choose a stall that
is as far from other people as possible. To avoid confusion, they
follow deterministic rules: For each empty stall S, they compute two
values LS and RS, each of which is the number of empty stalls between
S and the closest occupied stall to the left or right,
respectively. Then they consider the set of stalls with the farthest
closest neighbor, that is, those S for which min(LS, RS) is
maximal. If there is only one such stall, they choose it; otherwise,
they choose the one among those where max(LS, RS) is maximal. If there
are still multiple tied stalls, they choose the leftmost stall among
those.

K people are about to enter the bathroom; each one will choose their
stall before the next arrives. Nobody will ever leave.

When the last person chooses their stall S, what will the values of
max(LS, RS) and min(LS, RS) be?

Solving this problem

This problem has 2 Small datasets and 1 Large dataset. You must solve
the first Small dataset before you can attempt the second Small
dataset. You will be able to retry either of the Small datasets (with
a time penalty). You will be able to make a single attempt at the
Large, as usual, only after solving both Small datasets.

Input

The first line of the input gives the number of test cases, T. T lines
follow. Each line describes a test case with two integers N and K, as
described above.

Output

For each test case, output one line containing Case #x: y z, where x
is the test case number (starting from 1), y is max(LS, RS), and z is
min(LS, RS) as calculated by the last person to enter the bathroom for
their chosen stall S.

Limits

1 ≤ T ≤ 100.
1 ≤ K ≤ N.
Small dataset 1

1 ≤ N ≤ 1000.
Small dataset 2

1 ≤ N ≤ 106.
Large dataset

1 ≤ N ≤ 1018.
Sample


Input
-----

5
4 2
5 2
6 2
1000 1000
1000 1

Output
------

Case #1: 1 0
Case #2: 1 0
Case #3: 1 1
Case #4: 0 0
Case #5: 500 499

In Case #1, the first person occupies the leftmost of the middle two
stalls, leaving the following configuration (O stands for an occupied
stall and . for an empty one): [O.O..O]. Then, the second and last
person occupies the stall immediately to the right, leaving 1 empty
stall on one side and none on the other.

In Case #2, the first person occupies the middle stall, getting to
[O..O..O]. Then, the second and last person occupies the leftmost
stall.

In Case #3, the first person occupies the leftmost of the two middle
stalls, leaving [O..O...O]. The second person then occupies the middle
of the three consecutive empty stalls.

In Case #4, every stall is occupied at the end, no matter what the
stall choices are.

In Case #5, the first and only person chooses the leftmost middle
stall.


N = 5, N+2 stalls = 7 stalls, but 5 are free.
First guy picks 7 / 2.

"""


def free_stalls_left_to(stalls, position):
    if position >= len(stalls) or stalls[position] is not None:
        return 0
    free = 0
    for i in range(position - 1, -1, -1):
        if stalls[i] is None:
            free += 1
        else:
            break
    return free


def free_stalls_right_to(stalls, position):
    if position >= len(stalls) or stalls[position] is not None:
        return 0
    free = 0
    for i in range(position + 1, len(stalls)):
        if stalls[i] is None:
            free += 1
        else:
            break
    return free


def simulate_best_stall(stalls):
    computed_stalls = []
    for i, stall in enumerate(stalls):
        if stall is not None:
            continue
        left = free_stalls_left_to(stalls, i)
        right = free_stalls_right_to(stalls, i)
        computed_stalls.append((i, left, right,
                                min(left, right),
                                max(left, right)))
    best_min_distance = sorted(computed_stalls, key=lambda x: x[3])[-1][3]
    nice_stalls = [stall for stall in computed_stalls if
                   stall[3] == best_min_distance]
    best_max_distance = sorted(nice_stalls, key=lambda x: x[4])[-1][4]
    very_nice_stalls = [stall for stall in nice_stalls if
                        stall[4] == best_max_distance]

    return (min(stall[0] for stall in very_nice_stalls),
            best_max_distance,
            best_min_distance)



def simulate_choose_stall(qty_stalls, qty_human):
    stalls = [True] + [None for x in range(qty_stalls)] + [True]
    for h in range(qty_human - 1):
        # print("For", stalls, "choose", simulate_best_stall(stalls))
        stalls[simulate_best_stall(stalls)[0]] = True

    return simulate_best_stall(stalls)[1:]



if __name__ == '__main__':
    import sys
    test_cases = None
    case = 1
    with open(sys.argv[1]) as infile:
        for line in infile:
            line = line.strip()
            if test_cases is None:
                test_cases = line
                continue
            k, n = line.split()
            stats = simulate_choose_stall(int(k), int(n))
            print("Case #{}: {} {}".format(
                case, *stats))
            case += 1
