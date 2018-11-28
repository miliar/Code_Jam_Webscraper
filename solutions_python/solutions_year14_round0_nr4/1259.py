import sys


def solve(a_blocks, b_blocks):
    a_blocks = sorted(a_blocks)
    b_blocks = sorted(b_blocks)
    points = 0
    while b_blocks:
        if a_blocks[0] < b_blocks[0]:
            a_blocks = a_blocks[1:]
            b_blocks = b_blocks[:-1]
        else:
            a_blocks = a_blocks[1:]
            b_blocks = b_blocks[1:]
            points += 1

    return points


def solve_true(a_blocks, b_blocks):
    a_blocks = sorted(a_blocks)
    b_blocks = sorted(b_blocks)

    while b_blocks:
        to_beat = a_blocks[0]
        to_remove = None
        for x in b_blocks:
            if x > to_beat:
                to_remove = x
                break
        if not to_remove:
            return len(a_blocks)
        b_blocks.remove(to_remove)
        a_blocks.remove(to_beat)

    return 0

if __name__ == '__main__':
    f = open(sys.argv[1], 'r')

    cases = int(f.readline())
    for i in range(cases):
        num_of_blocks = int(f.readline())
        a_blocks = list(map(float, f.readline().split()))
        b_blocks = list(map(float, f.readline().split()))
        print('Case #{0}: {1} {2}'.format((i+1), solve(a_blocks[:], b_blocks[:]), solve_true(a_blocks[:], b_blocks[:])))

    f.close()
