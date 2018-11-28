import os, sys

lines = sys.stdin.read().split('\n')

lines.pop(0)

case = 0

mat = {
    (1, 1): (1, 1),
    (1, 'i'): (1, 'i'),
    (1, 'j'): (1, 'j'),
    (1, 'k'): (1, 'k'),
    ('i', 1): (1, 'i'),
    ('i', 'i'): (-1, 1),
    ('i', 'j'): (1, 'k'),
    ('i', 'k'): (-1, 'j'),
    ('j', 1): (1, 'j'),
    ('j', 'i'): (-1, 'k'),
    ('j', 'j'): (-1, 1),
    ('j', 'k'): (1, 'i'),
    ('k', 1): (1, 'k'),
    ('k', 'i'): (1, 'j'),
    ('k', 'j'): (-1, 'i'),
    ('k', 'k'): (-1, 1),
}

def mul(a, b):
    result = mat[(a[1], b[1])]
    return (result[0] * a[0] * b[0], result[1])

while lines:
    line = lines.pop(0)

    if not line:
        break

    case += 1
    repeat = int(line.split()[1])
    str = lines.pop(0) * repeat
    expecteds = ['i', 'j', 'k']
    expected = expecteds.pop(0)
    res = (1, 1)
    for i in range(len(str)):
        c = str[i]
        res = mul(res, (1, c))
        if res == (1, expected):
            if not expecteds:
                break
            expected = expecteds.pop(0)
            res = (1, 1)

    # remains sholud be 1
    res = (1, 1)
    for c in str[i + 1:]:
        res = mul(res, (1, c))

    if (not expecteds) and (res == (1, 1)):
        answer = "YES"
    else:
        answer = "NO"

    print "Case #%d: %s" % (case, answer)
