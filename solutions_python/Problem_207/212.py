import sys


def main():
    cases = int(raw_input())
    for case in range(cases):
        n, r, o, y, g, b, v = map(int, raw_input().split(" "))
        sol = solve((r, o, y, g, b, v))
        print "Case #%d: %s" % (case + 1, sol)

def solve(colors):
    n = sum(colors)
    (r, o, y, g, b, v) = colors

    relevant = sorted([(r, "R"), (y, "Y"), (b, "B")], reverse=True, key=lambda elem: elem[0])

    a, b, c = relevant[0][0], relevant[1][0], relevant[2][0]
    A, B, C = relevant[0][1], relevant[1][1], relevant[2][1]
    
    if a > b+c:
        return "IMPOSSIBLE"
    
    ret = ""
    for i in range(a):
        ret += A
        if b+c > a-i:
            b -= 1
            c -= 1
            ret += B + C
        elif b > 0:
            b -= 1
            ret += B
        elif c > 0:
            c -= 1
            ret += C

    
    return ret


if __name__ == "__main__":
    main()
