#!/usr/bin/env python
import fileinput

def compute(x, r, c):
    if x == 1:
        return True

    area = r * c
    # impossible based on area
    if x > area:
        return False
    if area % x != 0:
        return False
    if x >= 7: # can create a hole which is non-winning
        return False

    if r < x and c < x:
        return False

    if min(r,c) == 1 and max(r,c) > 2 and x > 2:
        return False

    if x >= 4 and max(r,c) == x and min(r,c)*2 <= x:
        return False

    # can choose a dimension that doesn't fit
    root = x/2.
    if x > 2 and root > r or root > c:
        return False

    # tileable
    if r % x != 0 and c % x != 0:
        return False

    return True

def main():
    num_runs = None
    n = 1
    for line in fileinput.input():
        if num_runs is None:
            num_runs = int(line)
            if num_runs <= 0:
                break
            else:
                continue

        x, r, c = line.split(' ')
        x = int(x)
        r = int(r)
        c = int(c)

        print "Case #%d: %s" % (n, "GABRIEL" if compute(x, r, c) else "RICHARD")
        n += 1
        if n >num_runs:
            break

if __name__ == "__main__":
    main()
