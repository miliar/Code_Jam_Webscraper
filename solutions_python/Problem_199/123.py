def show(i, val):
    print "Case #%s: %s" % (i, val if val is not None else "IMPOSSIBLE")


def check(row):
    return all([el == "+" for el in row])


def sol(row, k):
    n = len(row)
    if check(row):
        return 0

    total = 0
    for i in xrange(n - k + 1):
        if row[i] == "-":
            for j in xrange(i, i + k):
                row[j] = "+" if row[j] == "-" else "-"
            total += 1

    if check(row):
        return total
    else:
        return None


if __name__ == "__main__":
    T = int(raw_input().strip())

    for i in xrange(1, T + 1):
        row, k = raw_input().strip().split()
        row, k, n = list(row), int(k), len(row)
        show(i, sol(row, k))

