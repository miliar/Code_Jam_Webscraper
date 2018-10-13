import math

def get_number_of_test_case():
    return int(raw_input().strip())

def ans(x, y, n):
    if n == 1:
        if abs(x) + abs(y) != 1:
            return False
        elif x == 1:
            return 'E'
        elif x == -1:
            return 'W'
        elif y == 1:
            return 'N'
        elif y == -1:
            return 'S'
    else:
        threshold = (n * (n - 1) / 2)
        for item in [[x + n, y, 'W',], [x - n, y, 'E',], [x, y + n, 'S',], [x, y - n, 'N',]]:
            if abs(item[0]) + abs(item[1]) <= threshold:
                result = ans(item[0], item[1], n - 1)
                if result:
                    return result + item[2]
        return False

def solve_case(t):
    x, y = [int(i) for i in raw_input().strip().split()]
    z = abs(x) + abs(y)
    n = int(math.ceil((math.sqrt(z * 8 + 1) - 1) / 2))

    found = False
    result = ''
    while not found:
        result = ans(x, y, n)
        if result:
            found = True
        n += 1

    print 'Case #%d: %s' % (t, result,)

T = get_number_of_test_case()
t = 1
while t <= T:
    solve_case(t)
    t += 1

