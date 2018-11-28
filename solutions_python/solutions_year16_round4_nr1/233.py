import itertools


def get_winner(a, b):
    if a == 0:
        if b == 2:
            return b
        else:
            return a

    elif a == 1:
        if b == 0:
            return b
        else:
            return a
    else:
        if b == 1:
            return b
        else:
            return a


def is_valid(comb):
    if len(comb) == 1:
        return True
    new_comb = []
    for i in range(len(comb) / 2):
        if comb[2 * i] == comb[2 * i + 1]:
            return False
        else:
            new_comb.append(get_winner(comb[2 * i], comb[2 * i + 1]))

    return is_valid(new_comb)


def solve(n, r, p, s):
    IMPOSSIBLE = "IMPOSSIBLE"
    dic = {1: "R", 0: "P", 2: "S"}
    for comb in sorted(set(itertools.permutations([1] * r + [0] * p + [2] * s, n))):
        if is_valid(comb):
            return reduce(lambda a, b: a + b, map(dic.get, comb))
    return IMPOSSIBLE


def main():
    with open("A-input.in") as fin:
        with open("A-output.out", 'w') as fout:
            num_t = int(fin.readline())
            for t in xrange(num_t):
                n, r, p, s = map(int, fin.readline().strip().split())
                fout.write("Case #%d: %s\n" % (t + 1, solve(2 ** n, r, p, s)))

main()