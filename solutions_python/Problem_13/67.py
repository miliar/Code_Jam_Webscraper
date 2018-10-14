OR, AND = 0, 1


def update_tree(values, gates):
    for i in xrange(len(gates) - 1, -1, -1):
        left = values[2 * i + 1]
        right = values[2 * i + 2]
        if gates[i] == OR:
            values[i] = left | right
        else:
            values[i] = left & right


def count_ones(i, n):
    return sum((i >> j) & 1 for j in xrange(n))


for case in xrange(input()):
    m, v = map(int, raw_input().split())
    values = []
    gates = []
    changeable = []
    for i in xrange((m - 1) // 2):
        g, c = map(int, raw_input().split())
        values.append(None)
        gates.append(AND if g == 1 else OR)
        if c:
            changeable.append(i)
    for i in xrange((m + 1) // 2):
        values.append(input())

    y = None
    for perm in xrange(2 ** len(changeable)):
        changes = count_ones(perm, len(changeable))
        if y is None or changes < y:
            perm_gates = list(gates)
            for i, c in enumerate(changeable):
                if perm & (1 << i):
                    perm_gates[c] ^= 1
            update_tree(values, perm_gates)
            if values[0] == v:
                y = changes
    print 'Case #%d: %s' % (case + 1, 'IMPOSSIBLE' if y is None else y)
