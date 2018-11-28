import sys

def compute_cookie_time(c, f, x):
    cps = 2
    t = 0.0
    # Keep producing farms until it's less optimal
    # We reset to 0 cookies every time we decide to make a farm
    while x / cps > x / (cps + f) + c / cps:
        t += c / cps
        cps += f
    #Now we're at 0 cookies with optimal infrastructure. BAKE THE COOKIES
    t += x / cps
    return t

if __name__ == '__main__':
    lines = sys.stdin.readlines()
    for index, line in enumerate(lines[1:]):
        c, f, x = [float(val) for val in line.split()]
        t = compute_cookie_time(c, f, x)
        print "Case #%s: %.7f" % (index + 1, t)
