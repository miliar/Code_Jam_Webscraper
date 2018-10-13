import sys


def get_horizontal(lawn, row):
    return lawn[row]


def get_vertical(lawn, col):
    return [row[col] for row in lawn]


def check_lawn(lawn):
    for y, row in enumerate(lawn):
        for x, cell in enumerate(row):
            h = get_horizontal(lawn, y)
            v = get_vertical(lawn, x)
            higher_h = [el for el in h if el > cell]
            higher_v = [el for el in v if el > cell]

            #print x, y, cell, ':', h, v
            if higher_h and higher_v:
                return False

    return True


def solve(filename):
    with open(filename, 'r') as input_f:
        T = int(input_f.readline())
        for x in range(0, T):
            M, N = map(int, input_f.readline().split())
            lawn = [map(int, input_f.readline().split()) for r in range(0, M)]

            r = check_lawn(lawn)

            if r:
                print "Case #%s: YES" % (x+1)
            else:
                print "Case #%s: NO" % (x+1)

if __name__ == '__main__':
    filename = sys.argv[1]
    solve(filename)
