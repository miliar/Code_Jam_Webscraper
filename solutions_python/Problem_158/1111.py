import sys

def winner(n, r, c):
    richard = "RICHARD"
    gabe = "GABRIEL"
    # can we have a hole?
    if n >= 7:
        return richard
    # Do we fit?
    if 2 * min(r, c) < n: # L shape attack!
        return richard
    # can we force a hole?
    if n == 6 and (r == 2 or c == 2):
        return richard
    # Do we divide the squares?
    if r*c % n != 0:
        return richard
    # Can rich simply long one gabe?
    if (r < n and c < n):
        return richard
    # is it splittable with a sticky bit?
    if (r < n - 1 or c < n - 1):
        bad = min(r,c)
        over = n - bad
        for i in range(over):
            if (r*c - i % n) != 0:
                return richard
    return gabe

def main(args):
    afile = open(args[0]).readlines()[1:]
    for i, line in enumerate(afile, 1):
        print ("Case #%s: %s" % (i, winner(*map(int, line.split()))))
   
main(sys.argv[1:])
