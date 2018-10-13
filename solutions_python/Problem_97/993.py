def recycles(n):
    s = str(n)
    for _ in xrange(len(s)):
        s = s[1:] + s[:1]
        if s[:1] != "0":
            yield int(s)

def find(a, b):
    total = 0
    couples = ()
    for n in xrange(a, b + 1):
        for m in recycles(n):
            if a <= n and n < m and m <= b:
                if (n, m) not in couples:
                    couples += (n, m),
                    total += 1
    return total

fin = open("C-small-attempt0.in")
fout = open("c.out.txt", "w")
t = int(fin.readline())

for i in xrange(t):
    a, b = map(int, fin.readline().split())
    line = "Case #%d: %d" % (i + 1, find(a, b))
    print line
    fout.write(line + "\n")

fin.close()
fout.close()