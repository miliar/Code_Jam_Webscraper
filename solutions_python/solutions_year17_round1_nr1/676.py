#!/usr/bin/env python2

def read_all():
    T = int(raw_input())
    return [read_test() for i in range(T)]

def read_test():
    R,C = map(int, raw_input().split())
    return R, C, [raw_input() for i in range(R)]

def solve_test(r,c, cake):
    if not cake: return []

    assert len(cake) == r
    assert len(cake[0]) == c

    y = 0
    while cake[y] == '?' * c:
        y += 1

    letters = []
    for x in range(c):
        if cake[y][x] != '?':
            letters.append((x, cake[y][x]))

    row = ''
    for x, letter in letters:
        row += letter * (x - len(row) + 1)
        assert len(row) == x + 1

    row += letters[-1][1] * (c - len(row))
    assert len(row) == c

    y += 1
    while y < len(cake) and cake[y] == '?' * c:
        y += 1

    rem = []
    if y < len(cake):
        rem = solve_test(r-y, c, cake[y:])

    return [row] * y + rem


if __name__ == '__main__':
    tests = read_all()
    for i, test in enumerate(tests):
        answer = solve_test(*test)

        print 'Case #%d:' % (i+1,)
        print '\n'.join(answer)
