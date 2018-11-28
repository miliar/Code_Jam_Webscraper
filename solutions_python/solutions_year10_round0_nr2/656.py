from collections import deque
import sys

try:import psyco;psyco.full()
except: pass

def gcd(a,b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def apocal(vals):
    v = min(vals)
    vals = [i - v for i in vals]
    vals.remove(0)

    dx = gcd(vals[0], vals[1]) if len(vals) == 2 else vals[0]

    k = 0
    while k * dx < v:
        k += 1
    return k * dx - v


if __name__ == "__main__":
    fname = sys.argv[1]
    lines = open(fname).readlines()
    C = int(lines.pop(0))
    for i in range(C):
        l = map(int, lines.pop(0).split())[1:]
        print "Case #" + str(i + 1) + ":", apocal(l)
