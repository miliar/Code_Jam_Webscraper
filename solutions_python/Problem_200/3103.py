T = int(raw_input())


def tidy(line):
    last = 0
    line = map(int, list(line))
    for x in range(1, len(line)):
        if line[x] > line[last]:
            last = x
        elif line[x] < line[last]:
            line[last] -= 1
            for y in range(last + 1, len(line)):
                line[y] = 9

    return int("".join(map(str, line)))

for t in range(T):
    N = raw_input()
    print "Case #%d: %s" % (t + 1, tidy(N))
