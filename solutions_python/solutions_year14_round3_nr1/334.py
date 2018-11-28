from fractions import Fraction, gcd
import math
import sys

def solve(prog, p, q):
    gen = 0
    cd = gcd(p, q)
    p /= cd
    q /= cd
    power = int(math.log(q, 2))
    if 2 ** power != q:
        return "impossible"
    if power > 40:
        return "impossible"
    maxfact = q
    while True:
        if p >= maxfact:
            break
        maxfact /= 2
    ans = int(math.log(q / maxfact, 2))
    return ans

def main():
    T = int(sys.stdin.readline())
    for i in range(T):
        prog = i + 1
        p, q = sys.stdin.readline().split("/")
        print "Case #{0}: {1}".format(prog, solve(prog, int(p), int(q)))

main()
