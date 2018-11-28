from sys import argv


def find_last_tidy(x):
    xi = map(int, list(x))
    tidy_rev = []
    tidy_len = len(x)
    sbtrct = False
    for ir in range(len(xi))[::-1]:
        if ir > 0 and (xi[ir] < xi[ir - 1] or xi[ir - 1] == 0):
            if tidy_rev:
                tidy_rev[-1] = 9
            tidy_rev.append(9)
            sbtrct = True
        elif sbtrct and xi[ir] > 0:
            if ir > 0 and xi[ir] - 1 < xi[ir - 1]:
                if tidy_rev:
                    tidy_rev[-1] = 9
                tidy_rev.append(9)

                sbtrct = True
            else:
                tidy_rev.append(xi[ir] - 1)
                sbtrct = False
        elif sbtrct:
            if tidy_rev:
                tidy_rev[-1] = 9

            tidy_rev[-1] = 9
            tidy_rev.append(9)
        else:
            tidy_rev.append(xi[ir])
    tidy_rev = map(str, tidy_rev)
    tidy = "".join(tidy_rev[::-1]).lstrip('0')
    assert sorted(tidy) == list(tidy)
    return tidy


infile = argv[1]
with open(infile) as a:
    testcases = a.read().splitlines()[1:]

for i, case in enumerate(testcases):
    last_tidy = find_last_tidy(case)
    print "Case #{}: {}".format(i + 1, last_tidy)
