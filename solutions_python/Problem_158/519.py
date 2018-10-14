__author__ = 'Via'

# f = open('example_input.txt')
f = open('D-small-attempt0.in')
# f = open('C-large.in')
total_case = int(f.readline().strip())
file_out = open('output.txt', 'a')


def solve(x, r, c):
    if x == 1:
        return 'GABRIEL'
    if x == 2:
        if (r * c) % 2 == 0:
            return 'GABRIEL'
        else:
            return 'RICHARD'
    if x == 3:
        if (r * c) % 3 == 0:
            if r == 1 or c == 1:
                return 'RICHARD'
            else:
                return 'GABRIEL'
        else:
            return 'RICHARD'
    if x == 4:
        if (r * c) % 4 == 0:
            if r == 1 or c == 1:
                return 'RICHARD'
            elif r == 2 or c == 2:
                return 'RICHARD'
            elif r == 3 or c == 3:
                return 'GABRIEL'
            else:
                return 'GABRIEL'
        else:
            return 'RICHARD'


for i in range(total_case):
    x, r, c = map(int, f.readline().split())

    result = solve(x, r, c)
    print 'Case #{}: {}'.format(i + 1, result)
    file_out.writelines('Case #{}: {}\n'.format(i + 1, result))

file_out.close()