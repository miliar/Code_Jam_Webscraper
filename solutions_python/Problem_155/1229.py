from sys import stdin, stdout


def solve(shy_levels):
    standing = 0
    extra = 0
    for k, i in enumerate(shy_levels):
        need = max(0, k - standing)
        extra += need
        standing += int(i) + need
    return extra


if __name__ == "__main__":

    cases = int(stdin.readline())
    for c in xrange(1, cases + 1):
        _, shyness = stdin.readline().split()
        needed = solve(shyness)
        stdout.write("Case #{0}: {1}\n".format(c, needed))
