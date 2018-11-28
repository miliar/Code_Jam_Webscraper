import sys


def answer(n, pieces):
    full_x = []
    full_y = []
    full_sums = []
    full_diffs = []

    x_pos = set([])
    plus_pos = set([])
    for symbol, x, y in pieces:
        if symbol == 'x' or symbol == 'o':
            full_x.append(x)
            full_y.append(y)
            x_pos.add((x, y))
        if symbol == '+' or symbol == 'o':
            full_sums.append(x+y)
            full_diffs.append(x-y)
            plus_pos.add((x, y))

    free_x = [item for item in range(1, n+1) if item not in full_x]
    free_y = [item for item in range(1, n+1) if item not in full_y]
    free_sums = set([item for item in range(2, 2*n+1) if item not in full_sums])
    free_diffs = set([item for item in range(-(n-1), n) if item not in full_diffs])

    assert len(free_x) == len(free_y)
    assert len(free_sums) == len(free_diffs)

    new_x = set(zip(free_x, free_y))

    new_plus = set([])
    for x in range(1, n+1):
        for y in [1, n]:
            if x + y in free_sums and x - y in free_diffs:
                new_plus.add((x, y))
                free_sums -= set([x+y])
                free_diffs -= set([x - y])

    for y in range(1, n+1):
        for x in [1, n]:
            if x + y in free_sums and x - y in free_diffs:
                new_plus.add((x, y))
                free_sums -= set([x + y])
                free_diffs -= set([x - y])

    assert len(x_pos) + len(new_x) == n
    points = n + len(plus_pos) + len(new_plus)

    new_o = (new_plus & x_pos) | (new_x & plus_pos) | (new_plus & new_x)
    new_x -= new_o
    new_plus -= new_o
    assert not (new_x & x_pos)
    assert not (new_plus & plus_pos)

    number_of_added = len(new_x) + len(new_plus) + len(new_o)

    lines = [' '.join(map(str, [points, number_of_added]))]
    for x, y in new_x:
        lines.append(' '.join(['x', str(x), str(y)]))
    for x, y in new_plus:
        lines.append(' '.join(['+', str(x), str(y)]))
    for x, y in new_o:
        lines.append(' '.join(['o', str(x), str(y)]))

    total_o_set = (x_pos & plus_pos) | new_o
    total_x_set = (x_pos | new_x) - total_o_set
    total_plus_set = (plus_pos | new_plus) - total_o_set

    if not points == len(total_x_set) + len(total_plus_set) + 2*len(total_o_set):
        assert False

    total_rook_set = total_o_set | total_x_set
    total_bishop_set = total_o_set | total_plus_set
    assert len(total_rook_set) == n
    assert [sorted(item) for item in zip(*list(total_rook_set))] == [range(1, n+1), range(1, n+1)]
    assert len(total_bishop_set) == len(set([x - y for (x, y) in total_bishop_set]))
    assert len(total_bishop_set) == len(set([x + y for (x, y) in total_bishop_set]))

    return '\n'.join(lines)

if __name__ == "__main__":

    T = int(sys.stdin.next())
    queries = []
    for i in range(T):
        n, m = map(int, sys.stdin.next().split(' '))
        pieces = []
        for i in range(m):
            lst = sys.stdin.next().split(' ')
            lst[1:] = map(int, lst[1:])
            pieces.append(lst)
        queries.append((n, pieces))
    for i, qr in enumerate(queries):
        print "".join(["Case #", str(i+1), ": ", str(answer(*qr))])

