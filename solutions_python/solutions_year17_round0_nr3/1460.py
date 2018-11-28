#!/usr/bin/python
import math

def main():
    with open ('C-small-2-attempt0.in', 'r') as f, open('C-small-2-attempt0.out', 'w') as g:
        t = int(f.readline().strip())
        for i in xrange(1, t+1):
            a, b = [int(s) for s in f.readline().split()]
            c = 2**int(math.floor(math.log(b,2)))-1
            d = b - c
            e = a - c
            m = e - e / (c+1) * (c+1)
            n = e / (c+1)
            if d <= m:
                n = n + 1
            g.write("Case #{}: {} {}\n".format(i, str(n/2), str((n-1)/2)))


if __name__ == "__main__":
    main()