from sys import stdin

def add_sign(sign, result):
    if sign == 1:
        return result
    elif sign == -1:
        if result[0] == '-':
            return result[1:]
        else:
            return '-' + result
    else:
        assert False

def mul(a, b):
    sign = 1
    if a[0] == '-':
        sign = -sign
        a = a[1:]
    if b[0] == '-':
        sign = -sign
        b = b[1:]

    if a == '1':
        return add_sign(sign, b)
    if b == '1':
        return add_sign(sign, a)
    if a == b:
        return add_sign(sign, '-1')
    if a == 'i':
        if b == 'j':
            return add_sign(sign, 'k')
        if b == 'k':
            return add_sign(sign, '-j')
        assert False
    if a == 'j':
        if b == 'k':
            return add_sign(sign, 'i')
        if b == 'i':
            return add_sign(sign, '-k')
        assert False
    if a == 'k':
        if b == 'i':
            return add_sign(sign, 'j')
        if b == 'j':
            return add_sign(sign, '-i')
        assert False
    assert False

def accu_mul(ijk):
    if not ijk:
        return []
    accu = [ijk[0]]
    for s in ijk[1:]:
        accu.append(mul(accu[-1], s))
    return accu

def search(accu, target):
    for n, s in enumerate(accu):
        if s == target:
            return n + 1
    return 0

def each_case(X, spell):
    accu = accu_mul(spell)
    if accu[-1] == 1 or X % 4 == 0 or (X % 4 == 2 and accu[-1] == '-1') or (X % 2 != 0 and accu[-1] != '-1'):
        return 'NO'
    tmp = mul(accu[-1], 'i')

    position = search(accu, 'i')
    X -= 1
    if position == 0:
        position = search(accu, add_sign(-1, tmp))
        X -= 1
    if position == 0:
        position = search(accu, '-i')
        X -= 1
    if position == 0:
        position = search(accu, tmp)
        X -= 1
    if position == 0:
        return 'NO'
    
    accu_j = accu_mul(spell[position:])
    if accu_j:
        tmp_j = mul(accu_j[-1], 'j')
    else:
        tmp_j = 'j'
    tmp = mul(accu[-1], tmp_j)

    position = search(accu_j, 'j')
    if position == 0:
        position = search(accu, add_sign(-1, tmp_j))
        X -= 1
    if position == 0:
        position = search(accu, tmp)
        X -= 1
    if position == 0:
        position = search(accu, tmp_j)
        X -= 1
    if position == 0:
        position = search(accu, add_sign(-1, tmp))
        X -= 1
    if position == 0:
        return 'NO'

    if X < 0:
        return 'NO'
    return 'Yes'

T = int(stdin.readline())
for t in xrange(1,T+1):
    L, X = map(int, stdin.readline().split())
    spell = list(stdin.readline().strip())[:L]
    print 'Case #{}: {}'.format(t, each_case(X, spell))
