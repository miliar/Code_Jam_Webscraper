from solver import solver


def project(i, j, n):
    for di, li in [(-1, i), (+1, n-1-i)]:
        for dj, lj in [(-1, j), (+1, n-1-j)]:
            l = min(li, lj)
            yield i+di*l, j+dj*l


def border(n):
    m = n-1
    if m == 0:
        yield 0, 0
        return
    for x in range(m):
        yield 0, x
        yield x, m
        yield m, m-x
        yield m-x, 0


def solve_plus(pluses, n):
    valids = set(border(n))
    for i, j in pluses:
        valids -= set(project(i, j, n))
    while valids:
        i, j = valids.pop()
        yield i, j
        valids -= set(project(i, j, n))


def solve_cross(crosses, n):
    rows, columns = zip(*crosses) if crosses else ((), ())
    missing_rows = set(range(n)) - set(rows)
    missing_columns = set(range(n)) - set(columns)
    return zip(missing_rows, missing_columns)


@solver(lines_per_case="int(args[1])")
def fashion(lines):
    head, *lines = lines
    n, m = map(int, head.split())
    # Parse
    models = [line.split() for line in lines]
    pluses = [(int(x)-1, int(y)-1) for t, x, y in models if t in ['+', 'o']]
    crosses = [(int(x)-1, int(y)-1) for t, x, y in models if t in ['x', 'o']]
    circles = [(int(x)-1, int(y)-1) for t, x, y in models if t == 'o']
    # Solve pluses and crosses
    new_pluses = set(solve_plus(pluses, n))
    new_crosses = set(solve_cross(crosses, n))
    score = len(pluses) + len(crosses) + len(new_pluses) + len(new_crosses)
    # Solve circles
    all_circles = (set(pluses) | new_pluses) & (set(crosses) | new_crosses)
    new_circles = all_circles - set(circles)
    # Print
    results = []
    for i, j in (new_pluses - new_circles):
        results.append('{} {} {}'.format('+', i+1, j+1))
    for i, j in (new_crosses - new_circles):
        results.append('{} {} {}'.format('x', i+1, j+1))
    for i, j in new_circles:
        results.append('{} {} {}'.format('o', i+1, j+1))
    lines = ['{} {}'.format(score, len(results))] + results
    return '\n'.join(lines)


if __name__ == '__main__':
    fashion.from_cli()
