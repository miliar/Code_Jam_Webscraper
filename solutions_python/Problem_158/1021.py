import sys

# This one has some easy shortcuts: Any X >= 7 is guaranteed to be a richard win, because Richard can choose an X-omino that contains a central empty space. Also, if rXc is not evevenly divisible by X.
RICHARD = "RICHARD"
GABRIEL = "GABRIEL"

def main():
    f = sys.stdin
    tests = int(f.readline())
    for case in range(tests):
        xrc = f.readline().strip().split()
        x, r, c = map(int, xrc)
        print "Case #%d: %s" % (case + 1, tesselate(x, r, c))

def tesselate(x, r, c):
    # Returns a string referring to the winner of Ominous Omino (Google Codejam 2015-D)
    if x >= 7:
        return RICHARD
    if (r * c) % x:
        return RICHARD
    if (r * c) < (x * (x - 1)):
        return RICHARD
    if x <= 2:
        return GABRIEL
    if (r < x/2) or (c < x/2):
        return RICHARD
    return GABRIEL


if __name__ == "__main__":
    main()
