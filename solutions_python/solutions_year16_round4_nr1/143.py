def main():
    tn = int(raw_input())
    for ti in xrange(tn):
        n, r, p, s = map(int, raw_input().split(" "))
        x, y = 0, 1
        while x + x + y != r + p + s:
            x, y = (x+y), x+x
        if sorted([r, p, s]) != sorted([x, x, y]):
            print "Case #%d: %s" % (ti + 1, "IMPOSSIBLE")
        else:
            ans = solve(r, p, s)
            print "Case #%d: %s" % (ti + 1, ans)

def solve(r, p, s):
    if r+p+s == 1:
        if r == 1:
            return "R"
        elif p == 1:
            return "P"
        elif s == 1:
            return "S"
        else:
            raise Exception((r, p, s))
    if r == p:
        x = s / 2
        y = r - x
        a = solve(x, y, x)
        b = solve(y, x, x)
    elif p == s:
        x = r / 2
        y = p - x
        a = solve(x, y, x)
        b = solve(x, x, y)
    elif r == s:
        x = p / 2
        y = r - x
        a = solve(x, x, y)
        b = solve(y, x, x)
    else:
        raise Exception((r, p, s))
    return min(a, b) + max(a, b)

if __name__ == "__main__":
    main()
