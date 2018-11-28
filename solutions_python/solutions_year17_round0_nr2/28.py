import sys

if len(sys.argv) > 1:
    sys.stdin = open(sys.argv[1])


def good():
    return N[i] <= N[i+1]

for test in range(input()):
    print "Case #{}:".format(test+1),

    N = filter(lambda ch: 0 <= ch <= 9, map(lambda ch: ord(ch) - 48, raw_input()))

    l = len(N)

    i = 0

    while i < l-1 and good():
        i += 1

    if i < l-1:

        while i >= 0 and not good():
            N[i] -= 1
            N[i+1:] = [9] * (l-i-1)

            i -= 1

    if N[0] == 0:
        N = N[1:]

    print "".join(map(lambda x: chr(x+48), N))
