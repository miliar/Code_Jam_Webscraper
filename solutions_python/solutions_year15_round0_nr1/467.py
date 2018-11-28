fin = open("input.txt", "r")
fout = open("output.txt", "w")

T = int(fin.readline())

for _ in xrange(T):
    n, s = fin.readline().split()
    n = int(n)
    acc, res = 0, 0
    for i in xrange(len(s)):
        if acc < i:
            res += 1
            acc += 1
        acc += int(s[i])
    print >> fout, "Case #%d: %d" % (_ + 1, res)

fin.close()
fout.close()
