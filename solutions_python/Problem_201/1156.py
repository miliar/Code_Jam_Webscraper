import sys


def solve(n, k):
    # TODO Solve the problem

    ex = 2
    level = 1

    while ex * 2 - 1 < k:
        ex <<= 1

        level += 1

    cu = ex - 1
    remaining = k - cu

    """ Find frequency of empty spaces """
    freq = list()
    for i in range(level + 1):
        if i == 0:
            d = {
                n: 1
            }

            freq.append(d)
        else:
            d = dict()

            for k, v in freq[i - 1].iteritems():
                if k % 2 == 0:
                    if k / 2 - 1 in d:
                        d[k / 2 - 1] += v
                    else:
                        d[k / 2 - 1] = v

                    if k / 2 in d:
                        d[k / 2] += v
                    else:
                        d[k / 2] = v
                else:
                    if (k - 1) / 2 in d:
                        d[(k - 1) / 2] += 2 * v
                    else:
                        d[(k - 1) / 2] = 2 * v

            freq.append(d)

    start = n

    if remaining > 0:
        leaf_dict = freq[level]

        leaf_keys = list(leaf_dict.keys())
        leaf_keys.sort(reverse=True)

        for k in leaf_keys:
            v = leaf_dict[k]

            if remaining <= v:
                start = k
                break
            else:
                remaining -= v
    else:
        leaf_dict = freq[level - 1]

        leaf_keys = list(leaf_dict.keys())
        leaf_keys.sort()

        start = leaf_keys[0]

    if start % 2 == 0:
        return "{0} {1}".format(start / 2, start / 2 - 1)
    else:
        return "{0} {0}".format((start - 1) / 2)

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

    N, K = line.split()

    answer = solve(int(N), int(K))

    print 'Case #%d: %s' % (i, answer)
""" Interpret the arguments """
