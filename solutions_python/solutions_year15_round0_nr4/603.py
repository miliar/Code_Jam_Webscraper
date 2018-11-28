def solve(line):
    parts = line.split()
    parts = map(int, parts)
    x = parts[0]
    r = parts[1]
    c = parts[2]


    if (r * c) % x != 0:
        return False

    if r > c:
        long_side = r
        short_side = c
    else:
        long_side = c
        short_side = r

    i = 0
    while x - i >= 1 + i:
        if long_side < x - i or short_side < 1 + i:
            return False
        i += 1

    if x == 4 and long_side == 4 and short_side == 2:
        return False

    return True


if __name__ == "__main__":
    testcases = input()

    for case in xrange(1, testcases+1):
        line = raw_input()
        print("Case #%i: %s" % (case, 'GABRIEL' if solve(line) else 'RICHARD'))
