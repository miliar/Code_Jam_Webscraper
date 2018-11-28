import sys


quaternion = {
    '1': {
        '1': '1',
        'i': 'i',
        'j': 'j',
        'k': 'k',
    },
    'i': {
        '1': 'i',
        'i': '-1',
        'j': 'k',
        'k': '-j',
    },
    'j': {
        '1': 'j',
        'i': '-k',
        'j': '-1',
        'k': 'i',
    },
    'k': {
        '1': 'k',
        'i': 'j',
        'j': '-i',
        'k': '-1',
    }
}


def mul(a, b):
    sign = 1
    if a.startswith('-'):
        a = a[1:]
        sign *= -1
    if b.startswith('-'):
        b = b[1:]
        sign *= -1

    res = quaternion[a][b]
    if res.startswith('-'):
        sign *= -1

    if sign > 0 and res.startswith('-'):
        res = res[1:]
    elif sign < 0 and not res.startswith('-'):
        res = '-' + res

    return res


def solve_problem(s):
    i_positions = []
    k_positions = []

    product = '1'
    for i, c in enumerate(s):
        product = mul(product, c)

        if product == 'i':
            i_positions.append(i)

    if not i_positions:
        return "NO"

    product = '1'
    for k, c in enumerate(reversed(s)):
        product = mul(c, product)

        if product == 'k':
            k_positions.append(len(s) - k - 1)

    if not k_positions:
        return "NO"

    k_positions = sorted(k_positions)

    #print i_positions, k_positions
    #print len(i_positions), len(k_positions)

    for pos_i in i_positions:
        product = '1'
        last_pos = pos_i + 1
        for pos_k in k_positions:
            if pos_i >= pos_k:
                continue

            sub = s[last_pos:pos_k]
            #print "[{}:{}]".format(last_pos, pos_k), sub
            for c in sub:
                product = mul(product, c)

            if product == 'j':
                return "YES"

            last_pos = pos_k

    return "NO"


if __name__ == "__main__":
    num_of_cases = int(sys.stdin.readline().strip())

    for i in xrange(1, num_of_cases + 1):
        _, times = map(int, sys.stdin.readline().split())
        s = sys.stdin.readline().strip()
        print "Case #{0}: {1}".format(i, solve_problem(s * times))
