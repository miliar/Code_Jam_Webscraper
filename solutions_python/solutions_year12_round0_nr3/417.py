def recycle(n):
    l = len(str(n))
    ll = 10**(l - 1)
    for _ in range(l - 1):
        m = n % 10
        n = n / 10 + m * ll
        yield n


def compute(a, b):
    count = 0
    found = set()
    for n in range(a, b):
        for m in recycle(n):
            if n < m <= b and (n, m) not in found:
                found.add((n, m))
                count += 1
    return count


with open('C-large.in') as f, open('C-large.txt', 'w') as fout:
    ncases = int(f.readline())

    for i in range(ncases):
        a, b = (int(x) for x in f.readline().strip().split(" "))
        result = compute(a, b)
        fout.write("Case #%d: %d\n" % (i+1, result))
