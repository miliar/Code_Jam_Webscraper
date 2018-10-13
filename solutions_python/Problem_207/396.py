from sys import stdin
from math import inf

def solve(D):
    first = None
    last = None
    output = ""

    def P(x):
        return x[0] > 0 and x[1] is not last

    def C(x):
        if x[1] == first:
            return [inf, x[1]]
        else:
            return x

    while sum([x[0] for x in D]) > 0:
        try:
            x = sorted(filter(P, D), key=C, reverse=True)[0]
        except IndexError:
            return "IMPOSSIBLE"

        if not first:
            first = x[1]
        last = x[1]
        output += x[1]
        x[0] -= 1

    if output[0] == output[-1]:
        return "IMPOSSIBLE"
    else:
        return output

T = int(next(stdin))

for t in range(1, T+1):
    N, R, O, Y, G, B, V = map(int, next(stdin).strip().split(" "))

    print("Case #{0}: {1}".format(t, solve([[R, "R"], [O, "O"], [Y, "Y"], [G, "G"], [B, "B"], [V, "V"]])))
