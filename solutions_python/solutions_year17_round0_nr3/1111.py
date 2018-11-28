import math

with open("../files/" + 'Q2017C'[-1] + "-small-2-attempt0.in", 'r') as inp, open(
                    "../files/output" + 'Q2017C'[-1] + ".txt", 'w') as out:
    t = int(inp.readline())
    for i in xrange(t):
        string = "Case #" + str(i + 1) + ": {}"
        n, k = map(int, inp.readline().split())
        start = int(math.floor(math.log(k, 2)))
        diff = k - (1 << start)
        path = (diff << 1) + 1
        bin_path = bin(path)[2:][::-1]
        bin_path += "0" * (start + 1 - len(bin_path))
        for ch in bin_path[1:]:
            if ch == '0':
                n >>= 1
            else:
                n -= 1
                n >>= 1
        res = str(n >> 1) + " " + str((n - 1) >> 1)
        out.write(string.format(res) + "\n")
