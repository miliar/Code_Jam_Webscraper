import sys
import math


def r1(instream, type=int):
    return type(instream.readline().strip())


def ra(instream, type=int):
    return [type(x) for x in instream.readline().strip().split(" ")]


def solve_deceiful(naomi, ken):
    naomi = list(naomi)
    ken = list(ken)

    pt = 0
    while naomi:
        if naomi[0] > ken[0]:
            pt += 1
            ken.pop(0)
        else:
            ken.pop(-1)

        naomi.pop(0)

    return pt


def solve_normal(naomi, ken):
    naomi = list(naomi)
    ken = list(ken)

    pt = 0
    while naomi:
        if naomi[-1] > ken[-1]:
            pt += 1
            ken.pop(0)
        else:
            ken.pop(-1)

        naomi.pop(-1)
    
    return pt


def solve(instream):
    instream.readline()
    naomi = ra(instream, float)
    ken = ra(instream, float)

    naomi.sort()
    ken.sort()

    return "%s %s" % (solve_deceiful(naomi, ken), solve_normal(naomi, ken))
    

def run(input=sys.stdin):
    cases = int(input.readline().strip())
    for i in range(cases):
        print("Case #{}: {}".format(i + 1, solve(input)))

if __name__ == "__main__":
    run()
