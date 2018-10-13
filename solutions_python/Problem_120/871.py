import math
import sys
# Any ring requires r**2 - (r-1)**2 ml

memo = {}

def solve(r, t):
    solution = 0
    current = r + 1

    while True:
        first = memo.get(current)
        if not first:
            first = current ** 2
            memo[current] = first
        second = memo.get(current - 1)
        if not second:
            second = (current - 1) **2
            memo[current - 1] = second

        paint = first - second
        t = t - paint
        if t < 0:
            return solution
        solution += 1
        current += 2
    return 0

def parse(text):
    case = 1

    number, text = text.split('\n', 1)
    
    for test_case in text.split('\n'):
        if not test_case.strip():
            continue
        a, b = test_case.split()
        sol = solve(int(a), int(b))
        print "Case #%s: %s" % (case, sol)
        case += 1

if __name__ == "__main__":
    parse(sys.stdin.read())
