import sys
import os

def solve(p, f):
    flipCnt = 0

    def flip(startIndex):
        nonlocal flipCnt
        if startIndex + f > len(p):
            return False
        else:
            flipCnt += 1
            for i in range(startIndex, startIndex + f):
                p[i] = not(p[i])
            return True
    for i in range(len(p)):
        if not(p[i]) and not(flip(i)):
            return 'IMPOSSIBLE'
    return flipCnt

def main():
    with open(sys.argv[1]) as fp:
        def readline():
            return fp.readline().strip()
        num_cases = int(readline())
        with open(os.path.splitext(sys.argv[1])[0] + '.out', 'w') as fpo:
            for i in range(num_cases):
                p, f = readline().split()
                f = int(f)
                p = [x == '+' for x in p]
                res = "Case #%d: %s\n" % (i + 1, solve(p, f))
                print(res, end='')
                fpo.write(res)
main()
