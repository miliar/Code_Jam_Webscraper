def get_score(point):
    x = point / 3
    if point % 3 == 0:
        return x, x, x
    if point % 3 == 2:
        return x + 1, x + 1, x
    return x + 1, x, x

def compute(points, s, p):
    count = 0
    for point in points:
        m1, m2, _ = get_score(point)
        if m1 >= p:
            count += 1
        elif m1 == p - 1 and m2 == m1 and m2 > 0 and s > 0:
            count += 1
            s -= 1
    return count

with open('B-large.in') as f, open('B-large.txt', 'w') as fout:
    ncases = int(f.readline())

    for i in range(ncases):
        values = f.readline().strip().split(" ")
        s = int(values[1])
        p = int(values[2])
        points = [int(x) for x in values[3:]]
        assert len(points) == int(values[0])

        result = compute(points, s, p)
        fout.write("Case #%d: %d\n" % (i+1, result))
