def speed(d, n, ks):
    max_time = 0
    for i in ks:
        time = (d - i[0]) / i[1]
        max_time = max(time, max_time)
    return d / max_time

if __name__ == "__main__":
    with open("input") as fi,\
            open("output", "w") as fo:
        t = int(fi.readline())
        for i in range(1, t + 1):
            d, n = map(int, fi.readline().split())
            ks = []
            for j in range(n):
                ks.append(tuple(map(int, fi.readline().split())))
            fo.write("Case #{0}: {1:0.7f}\n".format(i, speed(d, n, ks)))
