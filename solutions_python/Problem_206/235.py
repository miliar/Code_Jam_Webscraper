name = "A-large"
input = name + ".in"
output = name + ".out"

def solve(d, n, k, s):
    t = [(d - k[i]) / float(s[i]) for i in range(n)]
    for i in range(n-2, -1, -1):
        t[i] = max(t[i], t[i+1])  # Can't pass

    print(t)

    return d / float(t[0])

line = -1
with open(input) as f:
    f_out = open(output, 'w')
    lines = f.readlines()

    def read_line():
        global line
        line += 1
        print(lines[line])
        return lines[line]

    t = int(read_line())

    for i in range(1, t+1):
        d, n = map(int, read_line().split())
        s = []
        k = []

        for _ in range(n):
            k_i, s_i = map(int, read_line().split())
            s.append(s_i)
            k.append(k_i)

        f_out.write("Case #%d: %f\n" % (i, solve(d, n, k, s)))