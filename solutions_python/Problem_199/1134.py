import sys


def merge(u, v):
    z = list()

    for i in range(len(u)):
        if u[i] == 0:
            if v[i] == 0:
                z.append(0)
            else:
                z.append(1)
        else:
            if v[i] == 0:
                z.append(1)
            else:
                z.append(0)

    return z


def solve(s, k):
    # TODO Solve the problem

    initial_plates = list()
    for x in s:
        if x == '-':
            initial_plates.append(0)
        else:
            initial_plates.append(1)

    target = [1 if x == 0 else 0 for x in initial_plates]
    num_pos = len(target) - k + 1

    components = list()
    for i in range(num_pos):
        v = [0] * len(target)

        v[i:(i + k)] = [1] * k

        components.append(v)

    term = [0] * len(target)
    num_flip = 0

    for i in range(num_pos):
        if target[i] != term[i]:
            term = merge(term, components[i])
            num_flip += 1

    if term != target:
        return "IMPOSSIBLE"

    return str(num_flip)

""" Convert the input file into a list of strings """
in_file = sys.argv[1]

with open(in_file, "r") as f:
    data = f.read()

lines = data.splitlines()
""" Convert the input file into a list of strings """

""" Interpret the arguments """
cases = int(lines.pop(0))

for i in range(1, cases + 1):
    line = lines.pop(0)
    S, K = line.split()

    answer = solve(S, int(K))

    print 'Case #%d: %s' % (i, answer)
""" Interpret the arguments """
