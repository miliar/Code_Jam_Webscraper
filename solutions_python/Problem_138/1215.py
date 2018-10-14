__author__ = 'PavelM'


def solve_war(n, a_blocks, b_blocks):
    j = 0
    w = 0
    for a in a_blocks:
        while j < n and a > b_blocks[j]:
            j += 1
        if j == n:
            break
        j += 1
        w += 1
    return n - w


def solve():
    n = int(in_file.readline())
    a_blocks = sorted(map(float, in_file.readline().split()))
    b_blocks = sorted(map(float, in_file.readline().split()))

    return n - solve_war(n, b_blocks, a_blocks), solve_war(n, a_blocks, b_blocks)



if __name__ == '__main__':
    name = 'D-large'
    with open('%s.out' % name, 'w') as output:
        with open('%s.in' % name) as in_file:
            n = int(in_file.readline())
            for k in range(1, n + 1):
                output.write('Case #{0}: {1} {2}\n'.format(k, *solve()))