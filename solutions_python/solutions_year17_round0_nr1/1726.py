import fileinput


def solve(s, k):
    r = 0
    i = 0
    s = list(s)
    while i < len(s)-(k-1):
        if s[i] == "-":
            r += 1
            for j in range(0, k):
                if s[i+j] == "-":
                    s[i+j] = "+"
                else:
                    s[i+j] = "-"
        i += 1

    for j in range(0, k):
        if s[len(s) - 1 - j] == "-":
            return "IMPOSSIBLE"

    return r

reader = fileinput.input()
t = int(reader.readline())
for i in range(1, t+1):
    s, k = [str(r) for r in reader.readline().split(" ")]
    print("Case #{}: {}".format(i, solve(s, int(k))))


