import numpy as np

def move_down(xs, ys, rs, i, x, y):
    result = 0
    xmin, xmax = x - rs[i], x + rs[i]
    for ii in xrange(i):
        if xs[ii] + rs[ii] <= xmin:
            continue
        if xs[ii] - rs[ii] >= xmax:
            continue
        result = max(result, ys[ii] + rs[ii] + rs[i])
    return result

def move_left(xs, ys, rs, i, x, y):
    result = 0
    ymin, ymax = y - rs[i], y + rs[i]
    for ii in xrange(i):
        if ys[ii] + rs[ii] <= ymin:
            continue
        if ys[ii] - rs[ii] >= ymax:
            continue
        result = max(result, xs[ii] + rs[ii] + rs[i])
    return result

def verify(xs, ys, rs):
    for i in range(len(xs)):
        for j in range(i+1, len(xs)):
            wid = rs[i] + rs[j]
            if abs(xs[i] - xs[j]) < wid and \
               abs(ys[i] - ys[j]) < wid:
                return False
    return True

def solve(w, h, rs):
    #greedy strategy
    #start in lower left, place things as far left/down as possible
    max_height = 0
    ind = np.argsort(rs).tolist()[::-1]
    r2s = [rs[i] for i in ind]
    xs = [None] * len(rs)
    ys = [None] * len(rs)
    for i in range(len(rs)):
        x, y = w, h
        while True:
            ynew = move_down(xs, ys, r2s, i, x, y)
            xnew = move_left(xs, ys, r2s, i, x, ynew)
            if xnew == x and ynew == y:
                break
            if xnew > x or ynew > y:
                break
            x, y = xnew, ynew
        xs[i] = x
        ys[i] = y
    assert verify(xs, ys, r2s)

    x2s = [0] * len(rs)
    y2s = [0] * len(rs)
    for i in range(len(rs)):
        x2s[ind[i]] = xs[i]
        y2s[ind[i]] = ys[i]
    return x2s, y2s

def main():
    from sys import argv
    data = open(argv[1]+'.in').readlines()
    ncase = int(data[0].strip())
    data = data[1:]
    with open(argv[1]+'.out', 'w') as outfile:
        for i in range(ncase):
            n,w,h = map(int, data[0].strip().split())
            rs = map(int, data[1].strip().split())
            xy = solve(w, h, rs)

            response = 'Case #%i:' % (i+1)
            for xx, yy in zip(*xy):
                response += ' %i %i' % (xx, yy)
            print response
            outfile.write(response+'\n')
            data = data[2:]


def test():
    w, h = 6, 6
    rs = [1, 1]
    print solve(w, h, rs)

    print solve(320, 2, [2, 3, 4])

if __name__ == "__main__":
    #print test()
    main()