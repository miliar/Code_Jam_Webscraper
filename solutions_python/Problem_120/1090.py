
import math
import sys

read = sys.stdin.readline

def root_sqr(a, b, c):
    return int((-b + math.sqrt(b * b - 4 * a * c)) / (2 * a))

def solve(r, t):
    return root_sqr(2, 2 * r - 1, - t)

def main():
    cases = int(read())
    for cs in range(1, cases+1):
        r, t = [int(x) for x in read().split()]
        print "Case #%s: %s" % (cs, solve(r, t))

if __name__ == '__main__':
    main() 
