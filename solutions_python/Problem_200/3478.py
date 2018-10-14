T = int(input())

case = 0


def dec(x):
    return str(int(x) - 1)


def tidy(orig):
    ii = 0
    ordered = ''

    while ii < len(orig) - 1 and orig[ii] <= orig[ii + 1]:
        ordered += orig[ii]
        ii += 1

    if ii == len(orig) - 1:
        return orig

    ordered = ordered + dec(orig[ii])

    suffix = ''.join(['9' for _ in range(len(orig) - len(ordered))])

    # print('ordered = ', ordered, ' suffix = ', suffix, ' ii = ', ii)

    while ii > 0 and ordered[ii - 1] > ordered[ii]:
        ordered = ordered[:ii - 1] + dec(ordered[ii - 1]) + '9' + ordered[ii + 1:]
        ii -= 1
        # print('ordered = ', ordered, ' suffix = ', suffix, ' ii = ', ii)

    # print('ordered = ', ordered, ' suffix = ', suffix, ' ii = ', ii)

    while len(ordered) > 0 and ordered[0] == '0':
        ordered = ordered[1:]

    return ordered + suffix


while case < T:
    case += 1
    orig = str(input())
    print("Case #{}: {}".format(case, tidy(orig)))
