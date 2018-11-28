"""Solve problem C of the qualification round of CodeWars 2017."""


def split(n):
    """Split a gap down the middle and return the gaps on either side."""
    if n % 2 != 0:
        return ((n - 1) // 2,
                (n - 1) // 2)
    else:
        return (n // 2,
                (n // 2) - 1)


def gen_new_level(prev_level):
    """Generate level after prev_level."""
    nums_from_prev = [pair[i] for i in range(2) for pair in prev_level]
    return [split(n) for n in nums_from_prev if n > 0]


def gen_tree(initial_num):
    """Yield levels of tree based on initial_num."""
    level = [split(initial_num)]
    yield level
    while level:
        level = gen_new_level(level)
        yield level


def solve(case):
    """Solve a given test case."""
    empty_stalls, people = case
    tree = gen_tree(empty_stalls)
    flat_tree = []
    for row in tree:
        try:
            gaps = flat_tree[people-1]
            return ' '.join(str(n) for n in gaps)
        except IndexError:
            flat_tree.extend(row)


def gen_cases():
    """Generate test cases."""
    n = 9
    for k in range(n):
        yield (n, k+1)


def solve_slow(case):
    """Solve a given test case in a much slower but correct way."""
    empty_stalls, people = case
    gaps = [empty_stalls]
    for p in range(people):
        largest_gap = gaps.pop()
        new_gaps = split(largest_gap)
        gaps.extend([gap for gap in new_gaps if gap > 0])
        gaps.sort()
    return '{} {}'.format(*new_gaps)


def test_solve(print_all=False):
    """Print differences between solve() and solve_slow()."""
    cases = gen_cases()
    if print_all:
        for i, case in enumerate(cases):
            print(
                'Case #{i} ({c}):'.format(i=i+1, c=case), end=' ', flush=True
            )
            fast_solution = solve(case)
            print(fast_solution, end=' ', flush=True)
            slow_solution = solve_slow(case)
            if fast_solution == slow_solution:
                print('\b')  # Get rid of that extra space
            else:
                print('({slow})'.format(slow=slow_solution))
    else:
        for i, case in enumerate(cases):
            fast_solution = solve(case)
            slow_solution = solve_slow(case)
            if fast_solution != slow_solution:
                print('Case #{i} ({c}): {fast} ({slow})'.format(
                    i=i+1, c=case, fast=fast_solution, slow=slow_solution
                ))


def smallest_discrepancy():
    """Return the smallest test case that causes the bug."""
    cases = gen_cases()
    for case in cases:
        slow_solution = solve_slow(case)
        fast_solution = solve(case)
        if fast_solution != slow_solution:
            return case, fast_solution, slow_solution


def main():
    """Call solve(case) for each case given."""
    cases = ((int(x) for x in input().split()) for __ in range(int(input())))
    # cases = gen_cases()
    for i, case in enumerate(cases):
        print('Case #{i}: {s}'.format(i=i+1, s=solve(case)))


if __name__ == '__main__':
    main()
