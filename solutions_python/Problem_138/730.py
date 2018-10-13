import sys, re

def choose_y(x, ys):
    min_i = -1
    for i in range(len(ys)):
        if ys[i] is not None:
            if min_i == -1:
                min_i = i
            if ys[i] > x:
                y = ys[i]
                ys[i] = None
                return y
    # no greater y found, so return smallest y
    y = ys[min_i]
    ys[min_i] = None
    return y

def solve(xs, ys):
    xs = sorted(xs)
    ys = sorted(ys)
    ys2 = list(ys)
    p = 0
    for x in xs:
        y = choose_y(x, ys)
        if y < x:
            p += 1
    # now play deceitful war
    q = 0
    ys = ys2
    i = 0
    l = len(xs)
    for j in range(l):
        while i < l and xs[i] < ys[j]:
            i += 1
        if i == l:
            break
        q += 1
        i += 1
    return (q, p)


def main(filename):
    with open(filename) as f_in:
        total = int(f_in.readline())
        for i in range(1, total+1):
            f_in.readline()
            xs = map(float, f_in.readline().strip().split(' '))
            ys = map(float, f_in.readline().strip().split(' '))
            (y, z) = solve(xs, ys)
            print 'Case #{0}: {1} {2}'.format(i, y, z)
            

if __name__ == "__main__":
    main(sys.argv[1])
