# f_name = 'sample.in'
# f_name = 'B-small-attempt2.in'
f_name = 'B-large.in'


def parse_input(str_test):
    t = str_test.split()
    n = map(int, list(t[0]))
    return n


def solve(test):
    ind = 0
    val = 0
    res = [None] * len(test)
    for i, d in enumerate(test):
        res[i] = d
        if d > val:
            ind = i
            val = d
        elif i > 0 and d < test[i - 1]:
            res[ind] = val - 1
            for j in range(ind + 1, len(test)):
                res[j] = 9
            break

    if res[0] == 0:
        del res[0]

    return ''.join(map(str, res))
