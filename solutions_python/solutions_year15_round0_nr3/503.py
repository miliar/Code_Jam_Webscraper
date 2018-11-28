import re
import sys


def parse(f):
    L, X = map(int, f.readline().strip().split())
    s = f.readline().strip()

    return L, X, s


def multiply(q, r):
    if q[0] == "-":
        if q[1] == "-":
            return multiply(q[2:], r)
        else:
            return "-" + multiply(q[1:], r)
    elif q == "1":
        return r
    elif q == "i":
        if r == "i":
            return "-1"
        elif r == "j":
            return "k"
        elif r == "k":
            return "-j"
    elif q == "j":
        if r == "i":
            return "-k"
        elif r == "j":
            return "-1"
        elif r == "k":
            return "i"
    elif q == "k":
        if r == "i":
            return "j"
        elif r =="j":
            return "-i"
        elif r == "k":
            return "-1"


def simplify(q):
    if q[:2] == "--":
        return simplify(q[2:])
    else:
        return q


def total(s):
    return reduce(multiply, s, "1")


def solve(L, X, s):
    MEMO = {}

    s = s*X
    if simplify(total(s)) != "-1":
        return False

    for i in xrange(1, L*X):
        if (0, i) in MEMO:
            prefix = MEMO[(0, i)]
        else:
            prefix = simplify(total(s[:i]))
            MEMO[(0, i)] = prefix

        if prefix != "i":
            continue

        for j in xrange(i+1, L*X):
            if (j, L*X) in MEMO:
                suffix = MEMO[(j, L*X)]
            else:
                suffix = simplify(total(s[j:]))
                MEMO[(j, L*X)] = suffix

            if suffix != "k":
                continue

            return True


def main():
    with open(sys.argv[1], "r") as input_file:
        T = int(input_file.readline())

        for i in xrange(T):
            L, X, s = parse(input_file)
            if solve(L, X, s):
                result = "YES"
            else:
                result = "NO"

            print "Case #%d: %s" % (i+1, result)


if __name__ == "__main__":
    main()
