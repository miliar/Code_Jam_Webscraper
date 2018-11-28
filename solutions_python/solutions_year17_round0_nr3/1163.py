

def solve(n, m):
    f = {n: 1}
    d = [n]

    def add(x, num):
        if x not in f:
            f[x] = 0
            d.append(x)
        f[x] += num

    i, j = 0, 0
    ans = None
    while j < m:
        if d[i] % 2 == 1:
            add(d[i] / 2, 2 * f[d[i]])
            ans = (d[i] / 2, d[i] / 2)
        else:
            add(d[i] / 2, f[d[i]])
            add(d[i] / 2 - 1, f[d[i]])
            ans = (d[i] / 2, d[i] / 2 - 1)
        j += f[d[i]]
        i += 1
    return ans

with file("3.txt", "r") as in_file:
    with file("ans.txt", "w") as out_file:
        i = 0
        for row in in_file:
            d = row.split()
            if len(d) < 2:
                continue
            i += 1
            print >>out_file, "Case #%d:"%i, " ".join(map(str, solve(int(d[0]), int(d[1]))))