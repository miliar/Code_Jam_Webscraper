def solve(x, r, c):
    if (r * c) % x != 0:
        return 'RICHARD'
    if x == 1 or x == 2:
        return 'GABRIEL'

    answers = {
        (3, 1, 3): False,
        (3, 1, 4): False,
        (3, 2, 2): False,
        (3, 2, 3): True,
        (3, 2, 4): False,
        (3, 3, 3): True,
        (3, 3, 4): True,
        (3, 4, 4): False,

        (4, 1, 4): False,
        (4, 2, 2): False,
        (4, 2, 3): False,
        (4, 2, 4): False,
        (4, 3, 3): False,
        (4, 3, 4): True,
        (4, 4, 4): True,
    }
    # for i in range(1, x + 1):
    #     v, h = i, (x + 1 - i)
    #     if v == 0 or h == 0:
    #         continue
    #     if v > max(r, c) or h > max(r, c):
    #         return 'RICHARD'
    #     if min(v, h) > min(r, c):
    #         return 'RICHARD'
    r, c = min(r, c), max(r, c)
    if answers[x, r, c]:
        return 'GABRIEL'
    return 'RICHARD'

input_file = open('d-small-3.txt')
cases = int(input_file.readline().strip())
case = 0
while case < cases:
    line = input_file.readline().strip().split(' ')
    X, R, C = [int(c) for c in line]
    minutes = solve(X, R, C)
    print "Case #{}: {}".format(case + 1, minutes)
    case += 1
